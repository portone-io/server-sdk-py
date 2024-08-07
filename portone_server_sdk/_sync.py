import dataclasses
import json
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Optional, TypeAliasType

import httpx
import serde

from ._api import ApiErrorResponse, ApiRequest, ApiSuccessResponse
from ._generated._env import user_agent

if TYPE_CHECKING:
    from _typeshed import DataclassInstance


@dataclass
class ApiClient:
    secret: str
    store_id: str | None = field(default=None, kw_only=True)
    api_base: str = field(default="https://api.portone.io", kw_only=True)

    client: httpx.Client = field(default_factory=httpx.Client, init=False)

    def __post_init__(self) -> None:
        self.client.base_url = httpx.URL(self.api_base)
        self.client.headers["Authentication"] = f"PortOne {self.secret}"
        if user_agent is not None:
            self.client.headers["User-Agent"] = user_agent

    def send[
        Success: DataclassInstance,
        Error: DataclassInstance,
        Param: DataclassInstance,
        Query: DataclassInstance,
        Body: DataclassInstance,
    ](
        self,
        request: ApiRequest[Success, Error, Param, Query, Body],
        success_cls: type[Success] | TypeAliasType,
        error_cls: type[Error] | TypeAliasType,
    ) -> ApiSuccessResponse[Success] | ApiErrorResponse[Error]:
        path = request.path
        for key, value in dataclasses.asdict(request.param).items():
            path = path.replace(f"{{{key}}}", value)
        query = dataclasses.asdict(request.query)
        body: Optional[dict[str, Any]] = None
        match request.method:
            case "get":
                asdict = dataclasses.asdict(request.body)
                if len(asdict) > 0:
                    query["requestBody"] = json.dumps(asdict)
            case "post":
                body = dataclasses.asdict(request.body)
        response = self.client.request(
            method=request.method,
            url=path,
            params=query,
            json=body,
        )
        if isinstance(success_cls, TypeAliasType):
            success_cls = success_cls.__value__
        if isinstance(error_cls, TypeAliasType):
            error_cls = error_cls.__value__
        if 200 <= response.status_code <= 299:
            return ApiSuccessResponse(serde.from_dict(success_cls, response.json()))
        return ApiErrorResponse(serde.from_dict(error_cls, response.json()))
