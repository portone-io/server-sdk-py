import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse, Empty
from portone_server_sdk._client import ApiClient
from portone_server_sdk import _errors
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._identity_verification_already_verified_error import IdentityVerificationAlreadyVerifiedError
from portone_server_sdk._openapi._schemas._identity_verification_not_found_error import IdentityVerificationNotFoundError
from portone_server_sdk._openapi._schemas._identity_verification_not_sent_error import IdentityVerificationNotSentError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._resend_identity_verification_error import ResendIdentityVerificationError
from portone_server_sdk._openapi._schemas._resend_identity_verification_response import ResendIdentityVerificationResponse
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class ResendIdentityVerificationParam:
    identity_verification_id: str = dataclasses.field(metadata={"serde_rename": "identityVerificationId"})
    """본인인증 아이디"""

@dataclasses.dataclass
class ResendIdentityVerificationQuery:
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId", "serde_skip_if": lambda value: value is None})
    """상점 아이디
    
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """

@dataclasses.dataclass
class ResendIdentityVerificationRequest(ApiRequest[ResendIdentityVerificationResponse, ResendIdentityVerificationError, ResendIdentityVerificationParam, ResendIdentityVerificationQuery, Empty]):
    method = "post"
    path = "/identity-verifications/{identityVerificationId}/resend"

@dataclasses.dataclass
class ResendIdentityVerification(ApiClient):
    def resend_identity_verification(
        self,
        *,
        identity_verification_id: str,
    ) -> ResendIdentityVerificationResponse:
        """SMS 본인인증 요청 재전송
        
        SMS 본인인증 요청을 재전송합니다.
        
        Args:
            identity_verification_id (str): 본인인증 아이디.
        
        Returns:
            성공 응답
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.IdentityVerificationAlreadyVerifiedError: 본인인증 건이 이미 인증 완료된 상태인 경우
            _errors.IdentityVerificationNotFoundError: 요청된 본인인증 건이 존재하지 않는 경우
            _errors.IdentityVerificationNotSentError: 본인인증 건이 API로 요청된 상태가 아닌 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = ResendIdentityVerificationParam(
            identity_verification_id=identity_verification_id,
        )
        query_ = ResendIdentityVerificationQuery(
            store_id=self.store_id,
        )
        body_ = Empty()
        response_ = self.send(
            ResendIdentityVerificationRequest(param_, query_, body_),
            ResendIdentityVerificationResponse,
            ResendIdentityVerificationError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            elif isinstance(error_, IdentityVerificationAlreadyVerifiedError):
                raise _errors.IdentityVerificationAlreadyVerifiedError(error_)
            elif isinstance(error_, IdentityVerificationNotFoundError):
                raise _errors.IdentityVerificationNotFoundError(error_)
            elif isinstance(error_, IdentityVerificationNotSentError):
                raise _errors.IdentityVerificationNotSentError(error_)
            elif isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            elif isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data

    async def resend_identity_verification_async(
        self,
        *,
        identity_verification_id: str,
    ) -> ResendIdentityVerificationResponse:
        """SMS 본인인증 요청 재전송
        
        SMS 본인인증 요청을 재전송합니다.
        
        Args:
            identity_verification_id (str): 본인인증 아이디.
        
        Returns:
            성공 응답
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.IdentityVerificationAlreadyVerifiedError: 본인인증 건이 이미 인증 완료된 상태인 경우
            _errors.IdentityVerificationNotFoundError: 요청된 본인인증 건이 존재하지 않는 경우
            _errors.IdentityVerificationNotSentError: 본인인증 건이 API로 요청된 상태가 아닌 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = ResendIdentityVerificationParam(
            identity_verification_id=identity_verification_id,
        )
        query_ = ResendIdentityVerificationQuery(
            store_id=self.store_id,
        )
        body_ = Empty()
        response_ = await self.send_async(
            ResendIdentityVerificationRequest(param_, query_, body_),
            ResendIdentityVerificationResponse,
            ResendIdentityVerificationError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            elif isinstance(error_, IdentityVerificationAlreadyVerifiedError):
                raise _errors.IdentityVerificationAlreadyVerifiedError(error_)
            elif isinstance(error_, IdentityVerificationNotFoundError):
                raise _errors.IdentityVerificationNotFoundError(error_)
            elif isinstance(error_, IdentityVerificationNotSentError):
                raise _errors.IdentityVerificationNotSentError(error_)
            elif isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            elif isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data
