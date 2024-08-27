import dataclasses
import json
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Optional, TypeVar, Union

import httpx
import serde

from portone_server_sdk._api import ApiErrorResponse, ApiRequest, ApiSuccessResponse
from portone_server_sdk._errors import UnknownError
from portone_server_sdk._generated._env import user_agent

if TYPE_CHECKING:
    from _typeshed import DataclassInstance
else:
    DataclassInstance = None

SuccessT = TypeVar("SuccessT", bound=DataclassInstance)
ErrorT = TypeVar("ErrorT", bound=DataclassInstance)
ParamT = TypeVar("ParamT", bound=DataclassInstance)
QueryT = TypeVar("QueryT", bound=DataclassInstance)
BodyT = TypeVar("BodyT", bound=DataclassInstance)


@dataclass
class ApiClient:
    secret: str
    store_id: Optional[str] = field(default=None)
    api_base: str = field(default="https://api.portone.io")

    client: httpx.Client = field(default_factory=httpx.Client, init=False)

    def __post_init__(self) -> None:
        self.client.base_url = httpx.URL(self.api_base)
        self.client.headers["Authorization"] = f"PortOne {self.secret}"
        if user_agent is not None:
            self.client.headers["User-Agent"] = user_agent

    def send(
        self,
        request: ApiRequest[SuccessT, ErrorT, ParamT, QueryT, BodyT],
        success_cls: Any,
        error_cls: Any,
    ) -> Union[ApiSuccessResponse[SuccessT], ApiErrorResponse[ErrorT]]:
        path = request.path
        for key, value in dataclasses.asdict(request.param).items():
            if value is not None:
                path = path.replace(f"{{{key}}}", value)
        query = dataclasses.asdict(
            request.query, dict_factory=lambda x: {k: v for k, v in x if v is not None}
        )
        body: Optional[dict[str, Any]] = None
        if request.method == "get" or request.method == "delete":
            asdict = dataclasses.asdict(
                request.body,
                dict_factory=lambda x: {k: v for k, v in x if v is not None},
            )
            if len(asdict) > 0:
                query["requestBody"] = json.dumps(asdict)
        if request.method == "post" or request.method == "patch":
            body = dataclasses.asdict(
                request.body,
                dict_factory=lambda x: {k: v for k, v in x if v is not None},
            )
        response = self.client.request(
            method=request.method,
            url=path,
            params=query,
            json=body,
        )
        if 200 <= response.status_code <= 299:
            return ApiSuccessResponse(
                serde.from_dict(serde.Untagged(success_cls), response.json())
            )
        try:
            return ApiErrorResponse(
                serde.from_dict(serde.Untagged(error_cls), response.json())
            )
        except Exception:
            raise UnknownError(response.text)
