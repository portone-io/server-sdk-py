import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse, Empty
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
from portone_server_sdk._openapi._schemas._billing_key_already_deleted_error import BillingKeyAlreadyDeletedError
from portone_server_sdk._openapi._schemas._billing_key_not_found_error import BillingKeyNotFoundError
from portone_server_sdk._openapi._schemas._billing_key_not_issued_error import BillingKeyNotIssuedError
from portone_server_sdk._openapi._schemas._channel_specific_error import ChannelSpecificError
from portone_server_sdk._openapi._schemas._delete_billing_key_error import DeleteBillingKeyError
from portone_server_sdk._openapi._schemas._delete_billing_key_response import DeleteBillingKeyResponse
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._payment_schedule_already_exists_error import PaymentScheduleAlreadyExistsError
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class DeleteBillingKeyParam:
    billingKey: str
    """삭제할 빌링키"""

@dataclasses.dataclass
class DeleteBillingKeyQuery:
    storeId: Optional[str]
    """상점 아이디
    
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """

@dataclasses.dataclass
class DeleteBillingKeyRequest(ApiRequest[DeleteBillingKeyResponse, DeleteBillingKeyError, DeleteBillingKeyParam, DeleteBillingKeyQuery, Empty]):
    method = "delete"
    path = "/billing-keys/{billingKey}"

@dataclasses.dataclass
class DeleteBillingKey(ApiClient):
    def delete_billing_key(
        self,
        billingKey: str,
        storeId: Optional[str],
    ) -> DeleteBillingKeyResponse:
        """빌링키 삭제
        
        빌링키를 삭제합니다.
        
        Args:
            billingKey (str): 삭제할 빌링키.
            storeId (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
        
        Returns:
            DeleteBillingKeyResponse: 성공 응답
        
        Raises:
            _errors.BillingKeyAlreadyDeletedError: 빌링키가 이미 삭제된 경우
            _errors.BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
            _errors.BillingKeyNotIssuedError: BillingKeyNotIssuedError
            _errors.ChannelSpecificError: 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PaymentScheduleAlreadyExistsError: 결제 예약건이 이미 존재하는 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = DeleteBillingKeyParam(
            billingKey=billingKey,
        )
        query_ = DeleteBillingKeyQuery(
            storeId=storeId,
        )
        body_ = Empty()
        response_ = self.send(
            DeleteBillingKeyRequest(param_, query_, body_),
            DeleteBillingKeyResponse,
            DeleteBillingKeyError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, BillingKeyAlreadyDeletedError):
                raise _errors.BillingKeyAlreadyDeletedError(error_)
            if isinstance(error_, BillingKeyNotFoundError):
                raise _errors.BillingKeyNotFoundError(error_)
            if isinstance(error_, BillingKeyNotIssuedError):
                raise _errors.BillingKeyNotIssuedError(error_)
            if isinstance(error_, ChannelSpecificError):
                raise _errors.ChannelSpecificError(error_)
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, PaymentScheduleAlreadyExistsError):
                raise _errors.PaymentScheduleAlreadyExistsError(error_)
            if isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
