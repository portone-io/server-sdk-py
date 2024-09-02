import dataclasses

from portone_server_sdk._api import ApiRequest, ApiErrorResponse, Empty
from portone_server_sdk import _errors
from portone_server_sdk._async import ApiClient
from portone_server_sdk._openapi._schemas._get_kakaopay_payment_order_error import GetKakaopayPaymentOrderError
from portone_server_sdk._openapi._schemas._get_kakaopay_payment_order_response import GetKakaopayPaymentOrderResponse
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class GetKakaopayPaymentOrderParam:
    pass

@dataclasses.dataclass
class GetKakaopayPaymentOrderQuery:
    pg_tx_id: str = dataclasses.field(metadata={"serde_rename": "pgTxId"})
    """카카오페이 주문 번호 (tid)"""
    channel_key: str = dataclasses.field(metadata={"serde_rename": "channelKey"})
    """채널 키"""

@dataclasses.dataclass
class GetKakaopayPaymentOrderRequest(ApiRequest[GetKakaopayPaymentOrderResponse, GetKakaopayPaymentOrderError, GetKakaopayPaymentOrderParam, GetKakaopayPaymentOrderQuery, Empty]):
    method = "get"
    path = "/kakaopay/payment/order"

@dataclasses.dataclass
class GetKakaopayPaymentOrder(ApiClient):
    async def get_kakaopay_payment_order(
        self,
        *,
        pg_tx_id: str,
        channel_key: str,
    ) -> GetKakaopayPaymentOrderResponse:
        """카카오페이 주문 조회 API
        
        주어진 아이디에 대응되는 카카오페이 주문 건을 조회합니다.
        해당 API 사용이 필요한 경우 포트원 기술지원팀으로 문의 주시길 바랍니다.
        
        Args:
            pg_tx_id (str): 카카오페이 주문 번호 (tid).
            channel_key (str): 채널 키.
        
        Returns:
            성공 응답으로 카카오페이 주문 조회 응답 객체를 반환합니다.
        
        Raises:
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = GetKakaopayPaymentOrderParam()
        query_ = GetKakaopayPaymentOrderQuery(
            pg_tx_id=pg_tx_id,
            channel_key=channel_key,
        )
        body_ = Empty()
        response_ = await self.send(
            GetKakaopayPaymentOrderRequest(param_, query_, body_),
            GetKakaopayPaymentOrderResponse,
            GetKakaopayPaymentOrderError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data
