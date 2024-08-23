import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._payment_not_found_error import PaymentNotFoundError
from portone_server_sdk._openapi._schemas._payment_not_paid_error import PaymentNotPaidError
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._register_store_receipt_body import RegisterStoreReceiptBody
from portone_server_sdk._openapi._schemas._register_store_receipt_body_item import RegisterStoreReceiptBodyItem
from portone_server_sdk._openapi._schemas._register_store_receipt_error import RegisterStoreReceiptError
from portone_server_sdk._openapi._schemas._register_store_receipt_response import RegisterStoreReceiptResponse
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class RegisterStoreReceiptParam:
    paymentId: str
    """등록할 하위 상점 결제 건 아이디"""

@dataclasses.dataclass
class RegisterStoreReceiptQuery:
    pass

@dataclasses.dataclass
class RegisterStoreReceiptRequest(ApiRequest[RegisterStoreReceiptResponse, RegisterStoreReceiptError, RegisterStoreReceiptParam, RegisterStoreReceiptQuery, RegisterStoreReceiptBody]):
    method = "post"
    path = "/payments/{paymentId}/register-store-receipt"

@dataclasses.dataclass
class RegisterStoreReceipt(ApiClient):
    def register_store_receipt(
        self,
        paymentId: str,
        items: list[RegisterStoreReceiptBodyItem],
        storeId: Optional[str],
    ) -> RegisterStoreReceiptResponse:
        """영수증 내 하위 상점 거래 등록
        
        결제 내역 매출전표에 하위 상점의 거래를 등록합니다.
        지원되는 PG사:
        KG이니시스(이용 전 콘솔 -> 결제연동 탭에서 INIApi Key 등록 필요)
        
        Args:
            paymentId (str): 등록할 하위 상점 결제 건 아이디.
            items (list[RegisterStoreReceiptBodyItem]): 하위 상점 거래 목록.
            storeId (Optional[str]): 상점 아이디.
        
        Returns:
            RegisterStoreReceiptResponse: 성공 응답
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PaymentNotFoundError: 결제 건이 존재하지 않는 경우
            _errors.PaymentNotPaidError: 결제가 완료되지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = RegisterStoreReceiptParam(
            paymentId=paymentId,
        )
        query_ = RegisterStoreReceiptQuery()
        body_ = RegisterStoreReceiptBody(
            items=items,
            storeId=storeId,
        )
        response_ = self.send(
            RegisterStoreReceiptRequest(param_, query_, body_),
            RegisterStoreReceiptResponse,
            RegisterStoreReceiptError,
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
