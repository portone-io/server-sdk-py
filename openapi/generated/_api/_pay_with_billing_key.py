import dataclasses
from typing import Any, Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk._client import ApiClient
from portone_server_sdk import _errors
from portone_server_sdk._openapi._schemas._already_paid_error import AlreadyPaidError
from portone_server_sdk._openapi._schemas._billing_key_already_deleted_error import BillingKeyAlreadyDeletedError
from portone_server_sdk._openapi._schemas._billing_key_not_found_error import BillingKeyNotFoundError
from portone_server_sdk._openapi._schemas._billing_key_payment_input import BillingKeyPaymentInput
from portone_server_sdk._openapi._schemas._cash_receipt_input import CashReceiptInput
from portone_server_sdk._openapi._schemas._channel_not_found_error import ChannelNotFoundError
from portone_server_sdk._openapi._schemas._country import Country
from portone_server_sdk._openapi._schemas._currency import Currency
from portone_server_sdk._openapi._schemas._customer_input import CustomerInput
from portone_server_sdk._openapi._schemas._discount_amount_exceeds_total_amount_error import DiscountAmountExceedsTotalAmountError
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._pay_with_billing_key_error import PayWithBillingKeyError
from portone_server_sdk._openapi._schemas._pay_with_billing_key_response import PayWithBillingKeyResponse
from portone_server_sdk._openapi._schemas._payment_amount_input import PaymentAmountInput
from portone_server_sdk._openapi._schemas._payment_product import PaymentProduct
from portone_server_sdk._openapi._schemas._payment_product_type import PaymentProductType
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._promotion_pay_method_does_not_match_error import PromotionPayMethodDoesNotMatchError
from portone_server_sdk._openapi._schemas._separated_address_input import SeparatedAddressInput
from portone_server_sdk._openapi._schemas._sum_of_parts_exceeds_total_amount_error import SumOfPartsExceedsTotalAmountError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class PayWithBillingKeyParam:
    payment_id: str = dataclasses.field(metadata={"serde_rename": "paymentId"})
    """결제 건 아이디"""

@dataclasses.dataclass
class PayWithBillingKeyQuery:
    pass

@dataclasses.dataclass
class PayWithBillingKeyRequest(ApiRequest[PayWithBillingKeyResponse, PayWithBillingKeyError, PayWithBillingKeyParam, PayWithBillingKeyQuery, BillingKeyPaymentInput]):
    method = "post"
    path = "/payments/{paymentId}/billing-key"

@dataclasses.dataclass
class PayWithBillingKey(ApiClient):
    def pay_with_billing_key(
        self,
        *,
        payment_id: str,
        billing_key: str,
        channel_key: Optional[str] = None,
        order_name: str,
        customer: Optional[CustomerInput] = None,
        custom_data: Optional[str] = None,
        amount: PaymentAmountInput,
        currency: Currency,
        installment_month: Optional[int] = None,
        use_free_interest_from_merchant: Optional[bool] = None,
        use_card_point: Optional[bool] = None,
        cash_receipt: Optional[CashReceiptInput] = None,
        country: Optional[Country] = None,
        notice_urls: Optional[list[str]] = None,
        products: Optional[list[PaymentProduct]] = None,
        product_count: Optional[int] = None,
        product_type: Optional[PaymentProductType] = None,
        shipping_address: Optional[SeparatedAddressInput] = None,
        promotion_id: Optional[str] = None,
        bypass: Optional[Any] = None,
    ) -> PayWithBillingKeyResponse:
        """빌링키 결제
        
        빌링키로 결제를 진행합니다.
        
        Args:
            payment_id (str): 결제 건 아이디.
            billing_key (str): 빌링키 결제에 사용할 빌링키.
            channel_key (Optional[str], optional): 채널 키.
                다수 채널에 대해 발급된 빌링키에 대해, 결제 채널을 특정하고 싶을 때 명시
            order_name (str): 주문명.
            customer (Optional[CustomerInput], optional): 고객 정보.
            custom_data (Optional[str], optional): 사용자 지정 데이터.
            amount (PaymentAmountInput): 결제 금액 세부 입력 정보.
            currency (Currency): 통화.
            installment_month (Optional[int], optional): 할부 개월 수.
            use_free_interest_from_merchant (Optional[bool], optional): 무이자 할부 이자를 고객사가 부담할지 여부.
            use_card_point (Optional[bool], optional): 카드 포인트 사용 여부.
            cash_receipt (Optional[CashReceiptInput], optional): 현금영수증 정보.
            country (Optional[Country], optional): 결제 국가.
            notice_urls (Optional[list[str]], optional): 웹훅 주소.
                결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
                상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            products (Optional[list[PaymentProduct]], optional): 상품 정보.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            product_count (Optional[int], optional): 상품 개수.
            product_type (Optional[PaymentProductType], optional): 상품 유형.
            shipping_address (Optional[SeparatedAddressInput], optional): 배송지 주소.
            promotion_id (Optional[str], optional): 해당 결제에 적용할 프로모션 아이디.
            bypass (Optional[Any], optional): PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고).
        
        Returns:
            성공 응답
        
        Raises:
            _errors.AlreadyPaidError: 결제가 이미 완료된 경우
            _errors.BillingKeyAlreadyDeletedError: 빌링키가 이미 삭제된 경우
            _errors.BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
            _errors.ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
            _errors.DiscountAmountExceedsTotalAmountError: 프로모션 할인 금액이 결제 시도 금액 이상인 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.PromotionPayMethodDoesNotMatchError: 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
            _errors.SumOfPartsExceedsTotalAmountError: 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = PayWithBillingKeyParam(
            payment_id=payment_id,
        )
        query_ = PayWithBillingKeyQuery()
        body_ = BillingKeyPaymentInput(
            store_id=self.store_id,
            billing_key=billing_key,
            channel_key=channel_key,
            order_name=order_name,
            customer=customer,
            custom_data=custom_data,
            amount=amount,
            currency=currency,
            installment_month=installment_month,
            use_free_interest_from_merchant=use_free_interest_from_merchant,
            use_card_point=use_card_point,
            cash_receipt=cash_receipt,
            country=country,
            notice_urls=notice_urls,
            products=products,
            product_count=product_count,
            product_type=product_type,
            shipping_address=shipping_address,
            promotion_id=promotion_id,
            bypass=bypass,
        )
        response_ = self.send(
            PayWithBillingKeyRequest(param_, query_, body_),
            PayWithBillingKeyResponse,
            PayWithBillingKeyError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, AlreadyPaidError):
                raise _errors.AlreadyPaidError(error_)
            elif isinstance(error_, BillingKeyAlreadyDeletedError):
                raise _errors.BillingKeyAlreadyDeletedError(error_)
            elif isinstance(error_, BillingKeyNotFoundError):
                raise _errors.BillingKeyNotFoundError(error_)
            elif isinstance(error_, ChannelNotFoundError):
                raise _errors.ChannelNotFoundError(error_)
            elif isinstance(error_, DiscountAmountExceedsTotalAmountError):
                raise _errors.DiscountAmountExceedsTotalAmountError(error_)
            elif isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            elif isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            elif isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            elif isinstance(error_, PromotionPayMethodDoesNotMatchError):
                raise _errors.PromotionPayMethodDoesNotMatchError(error_)
            elif isinstance(error_, SumOfPartsExceedsTotalAmountError):
                raise _errors.SumOfPartsExceedsTotalAmountError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data

    async def pay_with_billing_key_async(
        self,
        *,
        payment_id: str,
        billing_key: str,
        channel_key: Optional[str] = None,
        order_name: str,
        customer: Optional[CustomerInput] = None,
        custom_data: Optional[str] = None,
        amount: PaymentAmountInput,
        currency: Currency,
        installment_month: Optional[int] = None,
        use_free_interest_from_merchant: Optional[bool] = None,
        use_card_point: Optional[bool] = None,
        cash_receipt: Optional[CashReceiptInput] = None,
        country: Optional[Country] = None,
        notice_urls: Optional[list[str]] = None,
        products: Optional[list[PaymentProduct]] = None,
        product_count: Optional[int] = None,
        product_type: Optional[PaymentProductType] = None,
        shipping_address: Optional[SeparatedAddressInput] = None,
        promotion_id: Optional[str] = None,
        bypass: Optional[Any] = None,
    ) -> PayWithBillingKeyResponse:
        """빌링키 결제
        
        빌링키로 결제를 진행합니다.
        
        Args:
            payment_id (str): 결제 건 아이디.
            billing_key (str): 빌링키 결제에 사용할 빌링키.
            channel_key (Optional[str], optional): 채널 키.
                다수 채널에 대해 발급된 빌링키에 대해, 결제 채널을 특정하고 싶을 때 명시
            order_name (str): 주문명.
            customer (Optional[CustomerInput], optional): 고객 정보.
            custom_data (Optional[str], optional): 사용자 지정 데이터.
            amount (PaymentAmountInput): 결제 금액 세부 입력 정보.
            currency (Currency): 통화.
            installment_month (Optional[int], optional): 할부 개월 수.
            use_free_interest_from_merchant (Optional[bool], optional): 무이자 할부 이자를 고객사가 부담할지 여부.
            use_card_point (Optional[bool], optional): 카드 포인트 사용 여부.
            cash_receipt (Optional[CashReceiptInput], optional): 현금영수증 정보.
            country (Optional[Country], optional): 결제 국가.
            notice_urls (Optional[list[str]], optional): 웹훅 주소.
                결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
                상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            products (Optional[list[PaymentProduct]], optional): 상품 정보.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            product_count (Optional[int], optional): 상품 개수.
            product_type (Optional[PaymentProductType], optional): 상품 유형.
            shipping_address (Optional[SeparatedAddressInput], optional): 배송지 주소.
            promotion_id (Optional[str], optional): 해당 결제에 적용할 프로모션 아이디.
            bypass (Optional[Any], optional): PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고).
        
        Returns:
            성공 응답
        
        Raises:
            _errors.AlreadyPaidError: 결제가 이미 완료된 경우
            _errors.BillingKeyAlreadyDeletedError: 빌링키가 이미 삭제된 경우
            _errors.BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
            _errors.ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
            _errors.DiscountAmountExceedsTotalAmountError: 프로모션 할인 금액이 결제 시도 금액 이상인 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.PromotionPayMethodDoesNotMatchError: 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
            _errors.SumOfPartsExceedsTotalAmountError: 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = PayWithBillingKeyParam(
            payment_id=payment_id,
        )
        query_ = PayWithBillingKeyQuery()
        body_ = BillingKeyPaymentInput(
            store_id=self.store_id,
            billing_key=billing_key,
            channel_key=channel_key,
            order_name=order_name,
            customer=customer,
            custom_data=custom_data,
            amount=amount,
            currency=currency,
            installment_month=installment_month,
            use_free_interest_from_merchant=use_free_interest_from_merchant,
            use_card_point=use_card_point,
            cash_receipt=cash_receipt,
            country=country,
            notice_urls=notice_urls,
            products=products,
            product_count=product_count,
            product_type=product_type,
            shipping_address=shipping_address,
            promotion_id=promotion_id,
            bypass=bypass,
        )
        response_ = await self.send_async(
            PayWithBillingKeyRequest(param_, query_, body_),
            PayWithBillingKeyResponse,
            PayWithBillingKeyError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, AlreadyPaidError):
                raise _errors.AlreadyPaidError(error_)
            elif isinstance(error_, BillingKeyAlreadyDeletedError):
                raise _errors.BillingKeyAlreadyDeletedError(error_)
            elif isinstance(error_, BillingKeyNotFoundError):
                raise _errors.BillingKeyNotFoundError(error_)
            elif isinstance(error_, ChannelNotFoundError):
                raise _errors.ChannelNotFoundError(error_)
            elif isinstance(error_, DiscountAmountExceedsTotalAmountError):
                raise _errors.DiscountAmountExceedsTotalAmountError(error_)
            elif isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            elif isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            elif isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            elif isinstance(error_, PromotionPayMethodDoesNotMatchError):
                raise _errors.PromotionPayMethodDoesNotMatchError(error_)
            elif isinstance(error_, SumOfPartsExceedsTotalAmountError):
                raise _errors.SumOfPartsExceedsTotalAmountError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data
