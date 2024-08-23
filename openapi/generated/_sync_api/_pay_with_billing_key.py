import dataclasses
from typing import Any, Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
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
    paymentId: str
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
        paymentId: str,
        storeId: Optional[str],
        billingKey: str,
        channelKey: Optional[str],
        orderName: str,
        customer: Optional[CustomerInput],
        customData: Optional[str],
        amount: PaymentAmountInput,
        currency: Currency,
        installmentMonth: Optional[int],
        useFreeInterestFromMerchant: Optional[bool],
        useCardPoint: Optional[bool],
        cashReceipt: Optional[CashReceiptInput],
        country: Optional[Country],
        noticeUrls: Optional[list[str]],
        products: Optional[list[PaymentProduct]],
        productCount: Optional[int],
        productType: Optional[PaymentProductType],
        shippingAddress: Optional[SeparatedAddressInput],
        promotionId: Optional[str],
        bypass: Optional[Any],
    ) -> PayWithBillingKeyResponse:
        """빌링키 결제
        
        빌링키로 결제를 진행합니다.
        
        Args:
            paymentId (str): 결제 건 아이디.
            storeId (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
            billingKey (str): 빌링키 결제에 사용할 빌링키.
            channelKey (Optional[str]): 채널 키.
                다수 채널에 대해 발급된 빌링키에 대해, 결제 채널을 특정하고 싶을 때 명시
            orderName (str): 주문명.
            customer (Optional[CustomerInput]): 고객 정보.
            customData (Optional[str]): 사용자 지정 데이터.
            amount (PaymentAmountInput): 결제 금액 세부 입력 정보.
            currency (Currency): 통화.
            installmentMonth (Optional[int]): 할부 개월 수.
            useFreeInterestFromMerchant (Optional[bool]): 무이자 할부 이자를 고객사가 부담할지 여부.
            useCardPoint (Optional[bool]): 카드 포인트 사용 여부.
            cashReceipt (Optional[CashReceiptInput]): 현금영수증 정보.
            country (Optional[Country]): 결제 국가.
            noticeUrls (Optional[list[str]]): 웹훅 주소.
                결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
                상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            products (Optional[list[PaymentProduct]]): 상품 정보.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            productCount (Optional[int]): 상품 개수.
            productType (Optional[PaymentProductType]): 상품 유형.
            shippingAddress (Optional[SeparatedAddressInput]): 배송지 주소.
            promotionId (Optional[str]): 해당 결제에 적용할 프로모션 아이디.
            bypass (Optional[Any]): PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고).
        
        Returns:
            PayWithBillingKeyResponse: 성공 응답
        
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
            paymentId=paymentId,
        )
        query_ = PayWithBillingKeyQuery()
        body_ = BillingKeyPaymentInput(
            storeId=storeId,
            billingKey=billingKey,
            channelKey=channelKey,
            orderName=orderName,
            customer=customer,
            customData=customData,
            amount=amount,
            currency=currency,
            installmentMonth=installmentMonth,
            useFreeInterestFromMerchant=useFreeInterestFromMerchant,
            useCardPoint=useCardPoint,
            cashReceipt=cashReceipt,
            country=country,
            noticeUrls=noticeUrls,
            products=products,
            productCount=productCount,
            productType=productType,
            shippingAddress=shippingAddress,
            promotionId=promotionId,
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
            if isinstance(error_, BillingKeyAlreadyDeletedError):
                raise _errors.BillingKeyAlreadyDeletedError(error_)
            if isinstance(error_, BillingKeyNotFoundError):
                raise _errors.BillingKeyNotFoundError(error_)
            if isinstance(error_, ChannelNotFoundError):
                raise _errors.ChannelNotFoundError(error_)
            if isinstance(error_, DiscountAmountExceedsTotalAmountError):
                raise _errors.DiscountAmountExceedsTotalAmountError(error_)
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            if isinstance(error_, PromotionPayMethodDoesNotMatchError):
                raise _errors.PromotionPayMethodDoesNotMatchError(error_)
            if isinstance(error_, SumOfPartsExceedsTotalAmountError):
                raise _errors.SumOfPartsExceedsTotalAmountError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
