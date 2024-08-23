import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._async import ApiClient
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._get_payments_body import GetPaymentsBody
from portone_server_sdk._openapi._schemas._get_payments_error import GetPaymentsError
from portone_server_sdk._openapi._schemas._get_payments_response import GetPaymentsResponse
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._page_input import PageInput
from portone_server_sdk._openapi._schemas._payment_filter_input import PaymentFilterInput
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class GetPaymentsParam:
    pass

@dataclasses.dataclass
class GetPaymentsQuery:
    pass

@dataclasses.dataclass
class GetPaymentsRequest(ApiRequest[GetPaymentsResponse, GetPaymentsError, GetPaymentsParam, GetPaymentsQuery, GetPaymentsBody]):
    method = "get"
    path = "/payments"

@dataclasses.dataclass
class GetPayments(ApiClient):
    async def get_payments(
        self,
        page: Optional[PageInput],
        filter: Optional[PaymentFilterInput],
    ) -> GetPaymentsResponse:
        """결제 다건 조회(페이지 기반)
        
        주어진 조건에 맞는 결제 건들을 페이지 기반으로 조회합니다.
        
        Args:
            page (Optional[PageInput]): 요청할 페이지 정보.
                미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
            filter (Optional[PaymentFilterInput]): 조회할 결제 건 조건 필터.
                V1 결제 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
        
        Returns:
            GetPaymentsResponse: 성공 응답으로 조회된 결제 건 리스트와 페이지 정보가 반환됩니다.
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = GetPaymentsParam()
        query_ = GetPaymentsQuery()
        body_ = GetPaymentsBody(
            page=page,
            filter=filter,
        )
        response_ = await self.send(
            GetPaymentsRequest(param_, query_, body_),
            GetPaymentsResponse,
            GetPaymentsError,
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
