import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
from portone_server_sdk._openapi._schemas._already_paid_error import AlreadyPaidError
from portone_server_sdk._openapi._schemas._channel_not_found_error import ChannelNotFoundError
from portone_server_sdk._openapi._schemas._country import Country
from portone_server_sdk._openapi._schemas._currency import Currency
from portone_server_sdk._openapi._schemas._customer_input import CustomerInput
from portone_server_sdk._openapi._schemas._discount_amount_exceeds_total_amount_error import DiscountAmountExceedsTotalAmountError
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._instant_payment_input import InstantPaymentInput
from portone_server_sdk._openapi._schemas._instant_payment_method_input import InstantPaymentMethodInput
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._pay_instantly_error import PayInstantlyError
from portone_server_sdk._openapi._schemas._pay_instantly_response import PayInstantlyResponse
from portone_server_sdk._openapi._schemas._payment_amount_input import PaymentAmountInput
from portone_server_sdk._openapi._schemas._payment_product import PaymentProduct
from portone_server_sdk._openapi._schemas._payment_product_type import PaymentProductType
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._promotion_pay_method_does_not_match_error import PromotionPayMethodDoesNotMatchError
from portone_server_sdk._openapi._schemas._separated_address_input import SeparatedAddressInput
from portone_server_sdk._openapi._schemas._sum_of_parts_exceeds_total_amount_error import SumOfPartsExceedsTotalAmountError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class PayInstantlyParam:
    paymentId: str
    """결제 건 아이디"""

@dataclasses.dataclass
class PayInstantlyQuery:
    pass

@dataclasses.dataclass
class PayInstantlyRequest(ApiRequest[PayInstantlyResponse, PayInstantlyError, PayInstantlyParam, PayInstantlyQuery, InstantPaymentInput]):
    method = "post"
    path = "/payments/{paymentId}/instant"

@dataclasses.dataclass
class PayInstantly(ApiClient):
    def pay_instantly(
        self,
        paymentId: str,
        storeId: Optional[str],
        channelKey: Optional[str],
        channelGroupId: Optional[str],
        method: InstantPaymentMethodInput,
        orderName: str,
        isCulturalExpense: Optional[bool],
        isEscrow: Optional[bool],
        customer: Optional[CustomerInput],
        customData: Optional[str],
        amount: PaymentAmountInput,
        currency: Currency,
        country: Optional[Country],
        noticeUrls: Optional[list[str]],
        products: Optional[list[PaymentProduct]],
        productCount: Optional[int],
        productType: Optional[PaymentProductType],
        shippingAddress: Optional[SeparatedAddressInput],
        promotionId: Optional[str],
    ) -> PayInstantlyResponse:
        """수기 결제
        
        수기 결제를 진행합니다.
        
        Args:
            paymentId (str): 결제 건 아이디.
            storeId (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
            channelKey (Optional[str]): 채널 키.
                채널 키 또는 채널 그룹 ID 필수
            channelGroupId (Optional[str]): 채널 그룹 ID.
                채널 키 또는 채널 그룹 ID 필수
            method (InstantPaymentMethodInput): 결제수단 정보.
            orderName (str): 주문명.
            isCulturalExpense (Optional[bool]): 문화비 지출 여부.
                기본값은 false 입니다.
            isEscrow (Optional[bool]): 에스크로 결제 여부.
                기본값은 false 입니다.
            customer (Optional[CustomerInput]): 고객 정보.
            customData (Optional[str]): 사용자 지정 데이터.
            amount (PaymentAmountInput): 결제 금액 세부 입력 정보.
            currency (Currency): 통화.
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
        
        Returns:
            PayInstantlyResponse: 성공 응답
        
        Raises:
            _errors.AlreadyPaidError: 결제가 이미 완료된 경우
            _errors.ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
            _errors.DiscountAmountExceedsTotalAmountError: 프로모션 할인 금액이 결제 시도 금액 이상인 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.PromotionPayMethodDoesNotMatchError: 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
            _errors.SumOfPartsExceedsTotalAmountError: 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = PayInstantlyParam(
            paymentId=paymentId,
        )
        query_ = PayInstantlyQuery()
        body_ = InstantPaymentInput(
            storeId=storeId,
            channelKey=channelKey,
            channelGroupId=channelGroupId,
            method=method,
            orderName=orderName,
            isCulturalExpense=isCulturalExpense,
            isEscrow=isEscrow,
            customer=customer,
            customData=customData,
            amount=amount,
            currency=currency,
            country=country,
            noticeUrls=noticeUrls,
            products=products,
            productCount=productCount,
            productType=productType,
            shippingAddress=shippingAddress,
            promotionId=promotionId,
        )
        response_ = self.send(
            PayInstantlyRequest(param_, query_, body_),
            PayInstantlyResponse,
            PayInstantlyError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, AlreadyPaidError):
                raise _errors.AlreadyPaidError(error_)
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
