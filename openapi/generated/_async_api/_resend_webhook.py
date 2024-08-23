import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._async import ApiClient
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._payment_not_found_error import PaymentNotFoundError
from portone_server_sdk._openapi._schemas._resend_webhook_body import ResendWebhookBody
from portone_server_sdk._openapi._schemas._resend_webhook_error import ResendWebhookError
from portone_server_sdk._openapi._schemas._resend_webhook_response import ResendWebhookResponse
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError
from portone_server_sdk._openapi._schemas._webhook_not_found_error import WebhookNotFoundError

@dataclasses.dataclass
class ResendWebhookParam:
    paymentId: str
    """결제 건 아이디"""

@dataclasses.dataclass
class ResendWebhookQuery:
    pass

@dataclasses.dataclass
class ResendWebhookRequest(ApiRequest[ResendWebhookResponse, ResendWebhookError, ResendWebhookParam, ResendWebhookQuery, ResendWebhookBody]):
    method = "post"
    path = "/payments/{paymentId}/resend-webhook"

@dataclasses.dataclass
class ResendWebhook(ApiClient):
    async def resend_webhook(
        self,
        paymentId: str,
        storeId: Optional[str],
        webhookId: Optional[str],
    ) -> ResendWebhookResponse:
        """웹훅 재발송
        
        웹훅을 재발송합니다.
        
        Args:
            paymentId (str): 결제 건 아이디.
            storeId (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
            webhookId (Optional[str]): 웹훅 아이디.
                입력하지 않으면 결제 건의 가장 최근 웹훅 아이디가 기본 적용됩니다
        
        Returns:
            ResendWebhookResponse: 성공 응답
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PaymentNotFoundError: 결제 건이 존재하지 않는 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
            _errors.WebhookNotFoundError: 웹훅 내역이 존재하지 않는 경우
        """
        param_ = ResendWebhookParam(
            paymentId=paymentId,
        )
        query_ = ResendWebhookQuery()
        body_ = ResendWebhookBody(
            storeId=storeId,
            webhookId=webhookId,
        )
        response_ = await self.send(
            ResendWebhookRequest(param_, query_, body_),
            ResendWebhookResponse,
            ResendWebhookError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, PaymentNotFoundError):
                raise _errors.PaymentNotFoundError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)
            if isinstance(error_, WebhookNotFoundError):
                raise _errors.WebhookNotFoundError(error_)

        return response_.data
