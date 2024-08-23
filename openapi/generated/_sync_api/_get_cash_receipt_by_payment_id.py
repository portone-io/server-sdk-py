import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse, Empty
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
from portone_server_sdk._openapi._schemas._cash_receipt import CashReceipt
from portone_server_sdk._openapi._schemas._cash_receipt_not_found_error import CashReceiptNotFoundError
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._get_cash_receipt_error import GetCashReceiptError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class GetCashReceiptByPaymentIdParam:
    paymentId: str
    """결제 건 아이디"""

@dataclasses.dataclass
class GetCashReceiptByPaymentIdQuery:
    storeId: Optional[str]
    """상점 아이디
    
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """

@dataclasses.dataclass
class GetCashReceiptByPaymentIdRequest(ApiRequest[CashReceipt, GetCashReceiptError, GetCashReceiptByPaymentIdParam, GetCashReceiptByPaymentIdQuery, Empty]):
    method = "get"
    path = "/payments/{paymentId}/cash-receipt"

@dataclasses.dataclass
class GetCashReceiptByPaymentId(ApiClient):
    def get_cash_receipt_by_payment_id(
        self,
        paymentId: str,
        storeId: Optional[str],
    ) -> CashReceipt:
        """현금 영수증 단건 조회
        
        주어진 결제 아이디에 대응되는 현금 영수증 내역을 조회합니다.
        
        Args:
            paymentId (str): 결제 건 아이디.
            storeId (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
        
        Returns:
            CashReceipt: 성공 응답으로 현금 영수증 객체를 반환합니다.
        
        Raises:
            _errors.CashReceiptNotFoundError: 현금영수증이 존재하지 않는 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = GetCashReceiptByPaymentIdParam(
            paymentId=paymentId,
        )
        query_ = GetCashReceiptByPaymentIdQuery(
            storeId=storeId,
        )
        body_ = Empty()
        response_ = self.send(
            GetCashReceiptByPaymentIdRequest(param_, query_, body_),
            CashReceipt,
            GetCashReceiptError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, CashReceiptNotFoundError):
                raise _errors.CashReceiptNotFoundError(error_)
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
