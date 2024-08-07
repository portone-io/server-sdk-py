from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from _typeshed import DataclassInstance


@dataclass
class Empty:
    pass


@dataclass(init=False, slots=True)
class ApiRequest[
    Success: DataclassInstance,
    Error: DataclassInstance,
    Param: DataclassInstance,
    Query: DataclassInstance,
    Body: DataclassInstance,
]:
    method: ClassVar[str]
    path: ClassVar[str]
    param: Param
    query: Query
    body: Body


@dataclass(init=False, slots=True)
class ApiResponse[Data: DataclassInstance]:
    data: Data


@dataclass
class ApiSuccessResponse[Data: DataclassInstance](ApiResponse[Data]):
    pass


@dataclass
class ApiErrorResponse[Data: DataclassInstance](ApiResponse[Data]):
    pass
