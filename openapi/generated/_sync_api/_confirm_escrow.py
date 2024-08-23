import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
from portone_server_sdk._openapi._schemas._confirm_escrow_body import ConfirmEscrowBody
from portone_server_sdk._openapi._schemas._confirm_escrow_error import ConfirmEscrowError
from portone_server_sdk._openapi._schemas._confirm_escrow_response import ConfirmEscrowResponse
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._payment_not_found_error import PaymentNotFoundError
from portone_server_sdk._openapi._schemas._payment_not_paid_error import PaymentNotPaidError
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class ConfirmEscrowParam:
    paymentId: str
    """결제 건 아이디"""

@dataclasses.dataclass
class ConfirmEscrowQuery:
    pass

@dataclasses.dataclass
class ConfirmEscrowRequest(ApiRequest[ConfirmEscrowResponse, ConfirmEscrowError, ConfirmEscrowParam, ConfirmEscrowQuery, ConfirmEscrowBody]):
    method = "post"
    path = "/payments/{paymentId}/escrow/complete"

@dataclasses.dataclass
class ConfirmEscrow(ApiClient):
    def confirm_escrow(
        self,
        paymentId: str,
        storeId: Optional[str],
        fromStore: Optional[bool],
    ) -> ConfirmEscrowResponse:
        """에스크로 구매 확정
        
        에스크로 결제를 구매 확정 처리합니다
        
        Args:
            paymentId (str): 결제 건 아이디.
            storeId (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
            fromStore (Optional[bool]): 확인 주체가 상점인지 여부.
                구매확정요청 주체가 고객사 관리자인지 구매자인지 구분하기 위한 필드입니다.
                네이버페이 전용 파라미터이며, 구분이 모호한 경우 고객사 관리자(true)로 입력합니다.
        
        Returns:
            ConfirmEscrowResponse: 성공 응답
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PaymentNotFoundError: 결제 건이 존재하지 않는 경우
            _errors.PaymentNotPaidError: 결제가 완료되지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = ConfirmEscrowParam(
            paymentId=paymentId,
        )
        query_ = ConfirmEscrowQuery()
        body_ = ConfirmEscrowBody(
            storeId=storeId,
            fromStore=fromStore,
        )
        response_ = self.send(
            ConfirmEscrowRequest(param_, query_, body_),
            ConfirmEscrowResponse,
            ConfirmEscrowError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, PaymentNotFoundError):
                raise _errors.PaymentNotFoundError(error_)
            if isinstance(error_, PaymentNotPaidError):
                raise _errors.PaymentNotPaidError(error_)
            if isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
