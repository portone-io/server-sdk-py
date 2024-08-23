import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
from portone_server_sdk._openapi._schemas._confirm_identity_verification_body import ConfirmIdentityVerificationBody
from portone_server_sdk._openapi._schemas._confirm_identity_verification_error import ConfirmIdentityVerificationError
from portone_server_sdk._openapi._schemas._confirm_identity_verification_response import ConfirmIdentityVerificationResponse
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._identity_verification_already_verified_error import IdentityVerificationAlreadyVerifiedError
from portone_server_sdk._openapi._schemas._identity_verification_not_found_error import IdentityVerificationNotFoundError
from portone_server_sdk._openapi._schemas._identity_verification_not_sent_error import IdentityVerificationNotSentError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class ConfirmIdentityVerificationParam:
    identityVerificationId: str
    """본인인증 아이디"""

@dataclasses.dataclass
class ConfirmIdentityVerificationQuery:
    pass

@dataclasses.dataclass
class ConfirmIdentityVerificationRequest(ApiRequest[ConfirmIdentityVerificationResponse, ConfirmIdentityVerificationError, ConfirmIdentityVerificationParam, ConfirmIdentityVerificationQuery, ConfirmIdentityVerificationBody]):
    method = "post"
    path = "/identity-verifications/{identityVerificationId}/confirm"

@dataclasses.dataclass
class ConfirmIdentityVerification(ApiClient):
    def confirm_identity_verification(
        self,
        identityVerificationId: str,
        storeId: Optional[str],
        otp: Optional[str],
    ) -> ConfirmIdentityVerificationResponse:
        """본인인증 확인
        
        요청된 본인인증에 대한 확인을 진행합니다.
        
        Args:
            identityVerificationId (str): 본인인증 아이디.
            storeId (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
            otp (Optional[str]): OTP (One-Time Password).
                SMS 방식에서만 사용됩니다.
        
        Returns:
            ConfirmIdentityVerificationResponse: 성공 응답
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.IdentityVerificationAlreadyVerifiedError: 본인인증 건이 이미 인증 완료된 상태인 경우
            _errors.IdentityVerificationNotFoundError: 요청된 본인인증 건이 존재하지 않는 경우
            _errors.IdentityVerificationNotSentError: 본인인증 건이 API로 요청된 상태가 아닌 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = ConfirmIdentityVerificationParam(
            identityVerificationId=identityVerificationId,
        )
        query_ = ConfirmIdentityVerificationQuery()
        body_ = ConfirmIdentityVerificationBody(
            storeId=storeId,
            otp=otp,
        )
        response_ = self.send(
            ConfirmIdentityVerificationRequest(param_, query_, body_),
            ConfirmIdentityVerificationResponse,
            ConfirmIdentityVerificationError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, IdentityVerificationAlreadyVerifiedError):
                raise _errors.IdentityVerificationAlreadyVerifiedError(error_)
            if isinstance(error_, IdentityVerificationNotFoundError):
                raise _errors.IdentityVerificationNotFoundError(error_)
            if isinstance(error_, IdentityVerificationNotSentError):
                raise _errors.IdentityVerificationNotSentError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
