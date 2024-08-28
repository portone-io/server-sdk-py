import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._async import ApiClient
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
    payment_id: str = dataclasses.field(metadata={"serde_rename": "paymentId"})
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
    async def pay_instantly(
        self,
        payment_id: str,
        store_id: Optional[str],
        channel_key: Optional[str],
        channel_group_id: Optional[str],
        method: InstantPaymentMethodInput,
        order_name: str,
        is_cultural_expense: Optional[bool],
        is_escrow: Optional[bool],
        customer: Optional[CustomerInput],
        custom_data: Optional[str],
        amount: PaymentAmountInput,
        currency: Currency,
        country: Optional[Country],
        notice_urls: Optional[list[str]],
        products: Optional[list[PaymentProduct]],
        product_count: Optional[int],
        product_type: Optional[PaymentProductType],
        shipping_address: Optional[SeparatedAddressInput],
        promotion_id: Optional[str],
    ) -> PayInstantlyResponse:
        """수기 결제
        
        수기 결제를 진행합니다.
        
        Args:
            payment_id (str): 결제 건 아이디.
            store_id (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
            channel_key (Optional[str]): 채널 키.
                채널 키 또는 채널 그룹 ID 필수
            channel_group_id (Optional[str]): 채널 그룹 ID.
                채널 키 또는 채널 그룹 ID 필수
            method (InstantPaymentMethodInput): 결제수단 정보.
            order_name (str): 주문명.
            is_cultural_expense (Optional[bool]): 문화비 지출 여부.
                기본값은 false 입니다.
            is_escrow (Optional[bool]): 에스크로 결제 여부.
                기본값은 false 입니다.
            customer (Optional[CustomerInput]): 고객 정보.
            custom_data (Optional[str]): 사용자 지정 데이터.
            amount (PaymentAmountInput): 결제 금액 세부 입력 정보.
            currency (Currency): 통화.
            country (Optional[Country]): 결제 국가.
            notice_urls (Optional[list[str]]): 웹훅 주소.
                결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
                상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            products (Optional[list[PaymentProduct]]): 상품 정보.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
            product_count (Optional[int]): 상품 개수.
            product_type (Optional[PaymentProductType]): 상품 유형.
            shipping_address (Optional[SeparatedAddressInput]): 배송지 주소.
            promotion_id (Optional[str]): 해당 결제에 적용할 프로모션 아이디.
        
        Returns:
            성공 응답
        
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
            payment_id=payment_id,
        )
        query_ = PayInstantlyQuery()
        body_ = InstantPaymentInput(
            store_id=store_id,
            channel_key=channel_key,
            channel_group_id=channel_group_id,
            method=method,
            order_name=order_name,
            is_cultural_expense=is_cultural_expense,
            is_escrow=is_escrow,
            customer=customer,
            custom_data=custom_data,
            amount=amount,
            currency=currency,
            country=country,
            notice_urls=notice_urls,
            products=products,
            product_count=product_count,
            product_type=product_type,
            shipping_address=shipping_address,
            promotion_id=promotion_id,
        )
        response_ = await self.send(
            PayInstantlyRequest(param_, query_, body_),
            PayInstantlyResponse,
            PayInstantlyError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, AlreadyPaidError):
                raise _errors.AlreadyPaidError(error_)
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
