import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse, Empty
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
from portone_server_sdk._openapi._schemas._close_virtual_account_error import CloseVirtualAccountError
from portone_server_sdk._openapi._schemas._close_virtual_account_response import CloseVirtualAccountResponse
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._payment_not_found_error import PaymentNotFoundError
from portone_server_sdk._openapi._schemas._payment_not_waiting_for_deposit_error import PaymentNotWaitingForDepositError
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class CloseVirtualAccountParam:
    payment_id: str = dataclasses.field(metadata={"serde_rename": "paymentId"})
    """결제 건 아이디"""

@dataclasses.dataclass
class CloseVirtualAccountQuery:
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId", "serde_skip_if": lambda value: value is None})
    """상점 아이디
    
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """

@dataclasses.dataclass
class CloseVirtualAccountRequest(ApiRequest[CloseVirtualAccountResponse, CloseVirtualAccountError, CloseVirtualAccountParam, CloseVirtualAccountQuery, Empty]):
    method = "post"
    path = "/payments/{paymentId}/virtual-account/close"

@dataclasses.dataclass
class CloseVirtualAccount(ApiClient):
    def close_virtual_account(
        self,
        payment_id: str,
        store_id: Optional[str],
    ) -> CloseVirtualAccountResponse:
        """가상계좌 말소
        
        발급된 가상계좌를 말소합니다.
        
        Args:
            payment_id (str): 결제 건 아이디.
            store_id (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
        
        Returns:
            CloseVirtualAccountResponse: 성공 응답
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PaymentNotFoundError: 결제 건이 존재하지 않는 경우
            _errors.PaymentNotWaitingForDepositError: 결제 건이 입금 대기 상태가 아닌 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = CloseVirtualAccountParam(
            payment_id=payment_id,
        )
        query_ = CloseVirtualAccountQuery(
            store_id=store_id,
        )
        body_ = Empty()
        response_ = self.send(
            CloseVirtualAccountRequest(param_, query_, body_),
            CloseVirtualAccountResponse,
            CloseVirtualAccountError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            elif isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            elif isinstance(error_, PaymentNotFoundError):
                raise _errors.PaymentNotFoundError(error_)
            elif isinstance(error_, PaymentNotWaitingForDepositError):
                raise _errors.PaymentNotWaitingForDepositError(error_)
            elif isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data
