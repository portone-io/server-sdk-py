import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse, Empty
from portone_server_sdk._client import ApiClient
from portone_server_sdk import _errors
from portone_server_sdk._openapi._schemas._cancel_cash_receipt_error import CancelCashReceiptError
from portone_server_sdk._openapi._schemas._cancel_cash_receipt_response import CancelCashReceiptResponse
from portone_server_sdk._openapi._schemas._cash_receipt_not_found_error import CashReceiptNotFoundError
from portone_server_sdk._openapi._schemas._cash_receipt_not_issued_error import CashReceiptNotIssuedError
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class CancelCashReceiptByPaymentIdParam:
    payment_id: str = dataclasses.field(metadata={"serde_rename": "paymentId"})
    """결제 건 아이디"""

@dataclasses.dataclass
class CancelCashReceiptByPaymentIdQuery:
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId", "serde_skip_if": lambda value: value is None})
    """상점 아이디
    
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """

@dataclasses.dataclass
class CancelCashReceiptByPaymentIdRequest(ApiRequest[CancelCashReceiptResponse, CancelCashReceiptError, CancelCashReceiptByPaymentIdParam, CancelCashReceiptByPaymentIdQuery, Empty]):
    method = "post"
    path = "/payments/{paymentId}/cash-receipt/cancel"

@dataclasses.dataclass
class CancelCashReceiptByPaymentId(ApiClient):
    def cancel_cash_receipt_by_payment_id(
        self,
        *,
        payment_id: str,
    ) -> CancelCashReceiptResponse:
        """현금 영수증 취소
        
        현금 영수증 취소를 요청합니다.
        
        Args:
            payment_id (str): 결제 건 아이디.
        
        Returns:
            성공 응답
        
        Raises:
            _errors.CashReceiptNotFoundError: 현금영수증이 존재하지 않는 경우
            _errors.CashReceiptNotIssuedError: 현금영수증이 발급되지 않은 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = CancelCashReceiptByPaymentIdParam(
            payment_id=payment_id,
        )
        query_ = CancelCashReceiptByPaymentIdQuery(
            store_id=self.store_id,
        )
        body_ = Empty()
        response_ = self.send(
            CancelCashReceiptByPaymentIdRequest(param_, query_, body_),
            CancelCashReceiptResponse,
            CancelCashReceiptError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, CashReceiptNotFoundError):
                raise _errors.CashReceiptNotFoundError(error_)
            elif isinstance(error_, CashReceiptNotIssuedError):
                raise _errors.CashReceiptNotIssuedError(error_)
            elif isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            elif isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            elif isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data

    async def cancel_cash_receipt_by_payment_id_async(
        self,
        *,
        payment_id: str,
    ) -> CancelCashReceiptResponse:
        """현금 영수증 취소
        
        현금 영수증 취소를 요청합니다.
        
        Args:
            payment_id (str): 결제 건 아이디.
        
        Returns:
            성공 응답
        
        Raises:
            _errors.CashReceiptNotFoundError: 현금영수증이 존재하지 않는 경우
            _errors.CashReceiptNotIssuedError: 현금영수증이 발급되지 않은 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = CancelCashReceiptByPaymentIdParam(
            payment_id=payment_id,
        )
        query_ = CancelCashReceiptByPaymentIdQuery(
            store_id=self.store_id,
        )
        body_ = Empty()
        response_ = await self.send_async(
            CancelCashReceiptByPaymentIdRequest(param_, query_, body_),
            CancelCashReceiptResponse,
            CancelCashReceiptError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, CashReceiptNotFoundError):
                raise _errors.CashReceiptNotFoundError(error_)
            elif isinstance(error_, CashReceiptNotIssuedError):
                raise _errors.CashReceiptNotIssuedError(error_)
            elif isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            elif isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            elif isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data
