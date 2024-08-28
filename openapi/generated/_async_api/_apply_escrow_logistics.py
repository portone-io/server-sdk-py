import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._async import ApiClient
from portone_server_sdk._openapi._schemas._apply_escrow_logistics_error import ApplyEscrowLogisticsError
from portone_server_sdk._openapi._schemas._apply_escrow_logistics_response import ApplyEscrowLogisticsResponse
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._payment_escrow_receiver_input import PaymentEscrowReceiverInput
from portone_server_sdk._openapi._schemas._payment_escrow_sender_input import PaymentEscrowSenderInput
from portone_server_sdk._openapi._schemas._payment_logistics import PaymentLogistics
from portone_server_sdk._openapi._schemas._payment_not_found_error import PaymentNotFoundError
from portone_server_sdk._openapi._schemas._payment_not_paid_error import PaymentNotPaidError
from portone_server_sdk._openapi._schemas._payment_product import PaymentProduct
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._register_escrow_logistics_body import RegisterEscrowLogisticsBody
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class ApplyEscrowLogisticsParam:
    payment_id: str = dataclasses.field(metadata={"serde_rename": "paymentId"})
    """결제 건 아이디"""

@dataclasses.dataclass
class ApplyEscrowLogisticsQuery:
    pass

@dataclasses.dataclass
class ApplyEscrowLogisticsRequest(ApiRequest[ApplyEscrowLogisticsResponse, ApplyEscrowLogisticsError, ApplyEscrowLogisticsParam, ApplyEscrowLogisticsQuery, RegisterEscrowLogisticsBody]):
    method = "post"
    path = "/payments/{paymentId}/escrow/logistics"

@dataclasses.dataclass
class ApplyEscrowLogistics(ApiClient):
    async def apply_escrow_logistics(
        self,
        payment_id: str,
        store_id: Optional[str],
        sender: Optional[PaymentEscrowSenderInput],
        receiver: Optional[PaymentEscrowReceiverInput],
        logistics: PaymentLogistics,
        send_email: Optional[bool],
        products: Optional[list[PaymentProduct]],
    ) -> ApplyEscrowLogisticsResponse:
        """에스크로 배송 정보 등록
        
        에스크로 배송 정보를 등록합니다.
        
        Args:
            payment_id (str): 결제 건 아이디.
            store_id (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
            sender (Optional[PaymentEscrowSenderInput]): 에스크로 발송자 정보.
            receiver (Optional[PaymentEscrowReceiverInput]): 에스크로 수취인 정보.
            logistics (PaymentLogistics): 에스크로 물류 정보.
            send_email (Optional[bool]): 이메일 알림 전송 여부.
                에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
            products (Optional[list[PaymentProduct]]): 상품 정보.
        
        Returns:
            성공 응답
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PaymentNotFoundError: 결제 건이 존재하지 않는 경우
            _errors.PaymentNotPaidError: 결제가 완료되지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = ApplyEscrowLogisticsParam(
            payment_id=payment_id,
        )
        query_ = ApplyEscrowLogisticsQuery()
        body_ = RegisterEscrowLogisticsBody(
            store_id=store_id,
            sender=sender,
            receiver=receiver,
            logistics=logistics,
            send_email=send_email,
            products=products,
        )
        response_ = await self.send(
            ApplyEscrowLogisticsRequest(param_, query_, body_),
            ApplyEscrowLogisticsResponse,
            ApplyEscrowLogisticsError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            elif isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            elif isinstance(error_, PaymentNotFoundError):
                raise _errors.PaymentNotFoundError(error_)
            elif isinstance(error_, PaymentNotPaidError):
                raise _errors.PaymentNotPaidError(error_)
            elif isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data
