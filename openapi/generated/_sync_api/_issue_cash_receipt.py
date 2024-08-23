import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
from portone_server_sdk._openapi._schemas._cash_receipt_already_issued_error import CashReceiptAlreadyIssuedError
from portone_server_sdk._openapi._schemas._cash_receipt_type import CashReceiptType
from portone_server_sdk._openapi._schemas._channel_not_found_error import ChannelNotFoundError
from portone_server_sdk._openapi._schemas._currency import Currency
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._issue_cash_receipt_body import IssueCashReceiptBody
from portone_server_sdk._openapi._schemas._issue_cash_receipt_customer_input import IssueCashReceiptCustomerInput
from portone_server_sdk._openapi._schemas._issue_cash_receipt_error import IssueCashReceiptError
from portone_server_sdk._openapi._schemas._issue_cash_receipt_response import IssueCashReceiptResponse
from portone_server_sdk._openapi._schemas._payment_amount_input import PaymentAmountInput
from portone_server_sdk._openapi._schemas._payment_product_type import PaymentProductType
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class IssueCashReceiptParam:
    pass

@dataclasses.dataclass
class IssueCashReceiptQuery:
    pass

@dataclasses.dataclass
class IssueCashReceiptRequest(ApiRequest[IssueCashReceiptResponse, IssueCashReceiptError, IssueCashReceiptParam, IssueCashReceiptQuery, IssueCashReceiptBody]):
    method = "post"
    path = "/cash-receipts"

@dataclasses.dataclass
class IssueCashReceipt(ApiClient):
    def issue_cash_receipt(
        self,
        storeId: Optional[str],
        paymentId: str,
        channelKey: str,
        type: CashReceiptType,
        orderName: str,
        currency: Currency,
        amount: PaymentAmountInput,
        productType: Optional[PaymentProductType],
        customer: IssueCashReceiptCustomerInput,
        paidAt: Optional[str],
    ) -> IssueCashReceiptResponse:
        """현금 영수증 수동 발급
        
        현금 영수증 발급을 요청합니다.
        
        Args:
            storeId (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
            paymentId (str): 결제 건 아이디.
                외부 결제 건에 대한 수동 발급의 경우, 아이디를 직접 채번하여 입력합니다.
            channelKey (str): 채널 키.
            type (CashReceiptType): 현금 영수증 유형.
            orderName (str): 주문명.
            currency (Currency): 화폐.
            amount (PaymentAmountInput): 금액 세부 입력 정보.
            productType (Optional[PaymentProductType]): 상품 유형.
            customer (IssueCashReceiptCustomerInput): 고객 정보.
            paidAt (Optional[str]): 결제 일자.
        
        Returns:
            IssueCashReceiptResponse: 성공 응답
        
        Raises:
            _errors.CashReceiptAlreadyIssuedError: 현금영수증이 이미 발급된 경우
            _errors.ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = IssueCashReceiptParam()
        query_ = IssueCashReceiptQuery()
        body_ = IssueCashReceiptBody(
            storeId=storeId,
            paymentId=paymentId,
            channelKey=channelKey,
            type=type,
            orderName=orderName,
            currency=currency,
            amount=amount,
            productType=productType,
            customer=customer,
            paidAt=paidAt,
        )
        response_ = self.send(
            IssueCashReceiptRequest(param_, query_, body_),
            IssueCashReceiptResponse,
            IssueCashReceiptError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, CashReceiptAlreadyIssuedError):
                raise _errors.CashReceiptAlreadyIssuedError(error_)
            if isinstance(error_, ChannelNotFoundError):
                raise _errors.ChannelNotFoundError(error_)
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
