import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
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
    paymentId: str
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
    def modify_escrow_logistics(
        self,
        paymentId: str,
        storeId: Optional[str],
        sender: Optional[PaymentEscrowSenderInput],
        receiver: Optional[PaymentEscrowReceiverInput],
        logistics: PaymentLogistics,
        sendEmail: Optional[bool],
        products: Optional[list[PaymentProduct]],
    ) -> ModifyEscrowLogisticsResponse:
        """에스크로 배송 정보 수정
        
        에스크로 배송 정보를 수정합니다.
        
        Args:
            paymentId (str): 결제 건 아이디.
            storeId (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
            sender (Optional[PaymentEscrowSenderInput]): 에스크로 발송자 정보.
            receiver (Optional[PaymentEscrowReceiverInput]): 에스크로 수취인 정보.
            logistics (PaymentLogistics): 에스크로 물류 정보.
            sendEmail (Optional[bool]): 이메일 알림 전송 여부.
                에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
            products (Optional[list[PaymentProduct]]): 상품 정보.
        
        Returns:
            ModifyEscrowLogisticsResponse: 성공 응답
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PaymentNotFoundError: 결제 건이 존재하지 않는 경우
            _errors.PaymentNotPaidError: 결제가 완료되지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = ModifyEscrowLogisticsParam(
            paymentId=paymentId,
        )
        query_ = ModifyEscrowLogisticsQuery()
        body_ = ModifyEscrowLogisticsBody(
            storeId=storeId,
            sender=sender,
            receiver=receiver,
            logistics=logistics,
            sendEmail=sendEmail,
            products=products,
        )
        response_ = self.send(
            ModifyEscrowLogisticsRequest(param_, query_, body_),
            ModifyEscrowLogisticsResponse,
            ModifyEscrowLogisticsError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, PaymentNotFoundError):
                raise _errors.PaymentNotFoundError(error_)
            if isinstance(error_, PaymentNotPaidError):
                raise _errors.PaymentNotPaidError(error_)
            if isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
