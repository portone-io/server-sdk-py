import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk._client import ApiClient
from portone_server_sdk import _errors
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
        *,
        payment_id: str,
        channel_key: str,
        type: CashReceiptType,
        order_name: str,
        currency: Currency,
        amount: PaymentAmountInput,
        product_type: Optional[PaymentProductType] = None,
        customer: IssueCashReceiptCustomerInput,
        paid_at: Optional[str] = None,
    ) -> IssueCashReceiptResponse:
        """현금 영수증 수동 발급
        
        현금 영수증 발급을 요청합니다.
        
        Args:
            payment_id (str): 결제 건 아이디.
                외부 결제 건에 대한 수동 발급의 경우, 아이디를 직접 채번하여 입력합니다.
            channel_key (str): 채널 키.
            type (CashReceiptType): 현금 영수증 유형.
            order_name (str): 주문명.
            currency (Currency): 화폐.
            amount (PaymentAmountInput): 금액 세부 입력 정보.
            product_type (Optional[PaymentProductType], optional): 상품 유형.
            customer (IssueCashReceiptCustomerInput): 고객 정보.
            paid_at (Optional[str], optional): 결제 일자.
        
        Returns:
            성공 응답
        
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
            store_id=self.store_id,
            payment_id=payment_id,
            channel_key=channel_key,
            type=type,
            order_name=order_name,
            currency=currency,
            amount=amount,
            product_type=product_type,
            customer=customer,
            paid_at=paid_at,
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
            elif isinstance(error_, ChannelNotFoundError):
                raise _errors.ChannelNotFoundError(error_)
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

    async def issue_cash_receipt_async(
        self,
        *,
        payment_id: str,
        channel_key: str,
        type: CashReceiptType,
        order_name: str,
        currency: Currency,
        amount: PaymentAmountInput,
        product_type: Optional[PaymentProductType] = None,
        customer: IssueCashReceiptCustomerInput,
        paid_at: Optional[str] = None,
    ) -> IssueCashReceiptResponse:
        """현금 영수증 수동 발급
        
        현금 영수증 발급을 요청합니다.
        
        Args:
            payment_id (str): 결제 건 아이디.
                외부 결제 건에 대한 수동 발급의 경우, 아이디를 직접 채번하여 입력합니다.
            channel_key (str): 채널 키.
            type (CashReceiptType): 현금 영수증 유형.
            order_name (str): 주문명.
            currency (Currency): 화폐.
            amount (PaymentAmountInput): 금액 세부 입력 정보.
            product_type (Optional[PaymentProductType], optional): 상품 유형.
            customer (IssueCashReceiptCustomerInput): 고객 정보.
            paid_at (Optional[str], optional): 결제 일자.
        
        Returns:
            성공 응답
        
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
            store_id=self.store_id,
            payment_id=payment_id,
            channel_key=channel_key,
            type=type,
            order_name=order_name,
            currency=currency,
            amount=amount,
            product_type=product_type,
            customer=customer,
            paid_at=paid_at,
        )
        response_ = await self.send_async(
            IssueCashReceiptRequest(param_, query_, body_),
            IssueCashReceiptResponse,
            IssueCashReceiptError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, CashReceiptAlreadyIssuedError):
                raise _errors.CashReceiptAlreadyIssuedError(error_)
            elif isinstance(error_, ChannelNotFoundError):
                raise _errors.ChannelNotFoundError(error_)
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
