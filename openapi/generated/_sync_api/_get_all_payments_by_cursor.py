import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._get_all_payments_by_cursor_body import GetAllPaymentsByCursorBody
from portone_server_sdk._openapi._schemas._get_all_payments_by_cursor_response import GetAllPaymentsByCursorResponse
from portone_server_sdk._openapi._schemas._get_all_payments_error import GetAllPaymentsError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class GetAllPaymentsByCursorParam:
    pass

@dataclasses.dataclass
class GetAllPaymentsByCursorQuery:
    pass

@dataclasses.dataclass
class GetAllPaymentsByCursorRequest(ApiRequest[GetAllPaymentsByCursorResponse, GetAllPaymentsError, GetAllPaymentsByCursorParam, GetAllPaymentsByCursorQuery, GetAllPaymentsByCursorBody]):
    method = "get"
    path = "/payments-by-cursor"

@dataclasses.dataclass
class GetAllPaymentsByCursor(ApiClient):
    def get_all_payments_by_cursor(
        self,
        storeId: Optional[str],
        from_: Optional[str],
        until: Optional[str],
        cursor: Optional[str],
        size: Optional[int],
    ) -> GetAllPaymentsByCursorResponse:
        """결제 대용량 다건 조회(커서 기반)
        
        기간 내 모든 결제 건을 커서 기반으로 조회합니다. 결제 건의 생성일시를 기준으로 주어진 기간 내 존재하는 모든 결제 건이 조회됩니다.
        
        Args:
            storeId (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
            from_ (Optional[str]): 결제 건 생성시점 범위 조건의 시작.
                값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
            until (Optional[str]): 결제 건 생성시점 범위 조건의 끝.
                값을 입력하지 않으면 현재 시점으로 설정됩니다.
            cursor (Optional[str]): 커서.
                결제 건 리스트 중 어디서부터 읽어야 할지 가리키는 값입니다. 최초 요청일 경우 값을 입력하지 마시되, 두번째 요청 부터는 이전 요청 응답값의 cursor를 입력해주시면 됩니다.
            size (Optional[int]): 페이지 크기.
                미입력 시 기본값은 10 이며 최대 1000까지 허용
        
        Returns:
            GetAllPaymentsByCursorResponse: 성공 응답으로 조회된 결제 건 리스트와 커서 정보가 반환됩니다.
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = GetAllPaymentsByCursorParam()
        query_ = GetAllPaymentsByCursorQuery()
        body_ = GetAllPaymentsByCursorBody(
            storeId=storeId,
            from_=from_,
            until=until,
            cursor=cursor,
            size=size,
        )
        response_ = self.send(
            GetAllPaymentsByCursorRequest(param_, query_, body_),
            GetAllPaymentsByCursorResponse,
            GetAllPaymentsError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
