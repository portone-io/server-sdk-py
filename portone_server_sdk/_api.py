from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar

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
class Empty:
    pass


@dataclass(init=False)
class ApiRequest(
    Generic[
        SuccessT,
        ErrorT,
        ParamT,
        QueryT,
        BodyT,
    ]
):
    method: ClassVar[str]
    path: ClassVar[str]
    param: ParamT
    query: QueryT
    body: BodyT


DataT = TypeVar("DataT", bound=DataclassInstance)


@dataclass(init=False)
class ApiResponse(Generic[DataT]):
    data: DataT


@dataclass
class ApiSuccessResponse(ApiResponse[DataT]):
    pass


@dataclass
class ApiErrorResponse(ApiResponse[DataT]):
    pass
