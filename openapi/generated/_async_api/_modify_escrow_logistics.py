import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._async import ApiClient
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._modify_escrow_logistics_body import ModifyEscrowLogisticsBody
from portone_server_sdk._openapi._schemas._modify_escrow_logistics_error import ModifyEscrowLogisticsError
from portone_server_sdk._openapi._schemas._modify_escrow_logistics_response import ModifyEscrowLogisticsResponse
from portone_server_sdk._openapi._schemas._payment_escrow_receiver_input import PaymentEscrowReceiverInput
from portone_server_sdk._openapi._schemas._payment_escrow_sender_input import PaymentEscrowSenderInput
from portone_server_sdk._openapi._schemas._payment_logistics import PaymentLogistics
from portone_server_sdk._openapi._schemas._payment_not_found_error import PaymentNotFoundError
from portone_server_sdk._openapi._schemas._payment_not_paid_error import PaymentNotPaidError
from portone_server_sdk._openapi._schemas._payment_product import PaymentProduct
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class ModifyEscrowLogisticsParam:
    payment_id: str = dataclasses.field(metadata={"serde_rename": "paymentId"})
    """결제 건 아이디"""

@dataclasses.dataclass
class ModifyEscrowLogisticsQuery:
    pass

@dataclasses.dataclass
class ModifyEscrowLogisticsRequest(ApiRequest[ModifyEscrowLogisticsResponse, ModifyEscrowLogisticsError, ModifyEscrowLogisticsParam, ModifyEscrowLogisticsQuery, ModifyEscrowLogisticsBody]):
    method = "patch"
    path = "/payments/{paymentId}/escrow/logistics"

@dataclasses.dataclass
class ModifyEscrowLogistics(ApiClient):
    async def modify_escrow_logistics(
        self,
        *,
        payment_id: str,
        sender: Optional[PaymentEscrowSenderInput] = None,
        receiver: Optional[PaymentEscrowReceiverInput] = None,
        logistics: PaymentLogistics,
        send_email: Optional[bool] = None,
        products: Optional[list[PaymentProduct]] = None,
    ) -> ModifyEscrowLogisticsResponse:
        """에스크로 배송 정보 수정
        
        에스크로 배송 정보를 수정합니다.
        
        Args:
            payment_id (str): 결제 건 아이디.
            sender (Optional[PaymentEscrowSenderInput], optional): 에스크로 발송자 정보.
            receiver (Optional[PaymentEscrowReceiverInput], optional): 에스크로 수취인 정보.
            logistics (PaymentLogistics): 에스크로 물류 정보.
            send_email (Optional[bool], optional): 이메일 알림 전송 여부.
                에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
            products (Optional[list[PaymentProduct]], optional): 상품 정보.
        
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
        param_ = ModifyEscrowLogisticsParam(
            payment_id=payment_id,
        )
        query_ = ModifyEscrowLogisticsQuery()
        body_ = ModifyEscrowLogisticsBody(
            store_id=self.store_id,
            sender=sender,
            receiver=receiver,
            logistics=logistics,
            send_email=send_email,
            products=products,
        )
        response_ = await self.send(
            ModifyEscrowLogisticsRequest(param_, query_, body_),
            ModifyEscrowLogisticsResponse,
            ModifyEscrowLogisticsError,
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
