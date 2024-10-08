import dataclasses
from typing import Any, Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk._client import ApiClient
from portone_server_sdk import _errors
from portone_server_sdk._openapi._schemas._channel_not_found_error import ChannelNotFoundError
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._identity_verification_already_sent_error import IdentityVerificationAlreadySentError
from portone_server_sdk._openapi._schemas._identity_verification_already_verified_error import IdentityVerificationAlreadyVerifiedError
from portone_server_sdk._openapi._schemas._identity_verification_method import IdentityVerificationMethod
from portone_server_sdk._openapi._schemas._identity_verification_not_found_error import IdentityVerificationNotFoundError
from portone_server_sdk._openapi._schemas._identity_verification_operator import IdentityVerificationOperator
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._send_identity_verification_body import SendIdentityVerificationBody
from portone_server_sdk._openapi._schemas._send_identity_verification_body_customer import SendIdentityVerificationBodyCustomer
from portone_server_sdk._openapi._schemas._send_identity_verification_error import SendIdentityVerificationError
from portone_server_sdk._openapi._schemas._send_identity_verification_response import SendIdentityVerificationResponse
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class SendIdentityVerificationParam:
    identity_verification_id: str = dataclasses.field(metadata={"serde_rename": "identityVerificationId"})
    """본인인증 아이디"""

@dataclasses.dataclass
class SendIdentityVerificationQuery:
    pass

@dataclasses.dataclass
class SendIdentityVerificationRequest(ApiRequest[SendIdentityVerificationResponse, SendIdentityVerificationError, SendIdentityVerificationParam, SendIdentityVerificationQuery, SendIdentityVerificationBody]):
    method = "post"
    path = "/identity-verifications/{identityVerificationId}/send"

@dataclasses.dataclass
class SendIdentityVerification(ApiClient):
    def send_identity_verification(
        self,
        *,
        identity_verification_id: str,
        channel_key: str,
        customer: SendIdentityVerificationBodyCustomer,
        custom_data: Optional[str] = None,
        bypass: Optional[Any] = None,
        operator: IdentityVerificationOperator,
        method: IdentityVerificationMethod,
    ) -> SendIdentityVerificationResponse:
        """본인인증 요청 전송
        
        SMS 또는 APP 방식을 이용하여 본인인증 요청을 전송합니다.
        
        Args:
            identity_verification_id (str): 본인인증 아이디.
            channel_key (str): 채널 키.
            customer (SendIdentityVerificationBodyCustomer): 고객 정보.
            custom_data (Optional[str], optional): 사용자 지정 데이터.
            bypass (Optional[Any], optional): PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고).
            operator (IdentityVerificationOperator): 통신사.
            method (IdentityVerificationMethod): 본인인증 방식.
        
        Returns:
            성공 응답
        
        Raises:
            _errors.ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.IdentityVerificationAlreadySentError: 본인인증 건이 이미 API로 요청된 상태인 경우
            _errors.IdentityVerificationAlreadyVerifiedError: 본인인증 건이 이미 인증 완료된 상태인 경우
            _errors.IdentityVerificationNotFoundError: 요청된 본인인증 건이 존재하지 않는 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = SendIdentityVerificationParam(
            identity_verification_id=identity_verification_id,
        )
        query_ = SendIdentityVerificationQuery()
        body_ = SendIdentityVerificationBody(
            store_id=self.store_id,
            channel_key=channel_key,
            customer=customer,
            custom_data=custom_data,
            bypass=bypass,
            operator=operator,
            method=method,
        )
        response_ = self.send(
            SendIdentityVerificationRequest(param_, query_, body_),
            SendIdentityVerificationResponse,
            SendIdentityVerificationError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ChannelNotFoundError):
                raise _errors.ChannelNotFoundError(error_)
            elif isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            elif isinstance(error_, IdentityVerificationAlreadySentError):
                raise _errors.IdentityVerificationAlreadySentError(error_)
            elif isinstance(error_, IdentityVerificationAlreadyVerifiedError):
                raise _errors.IdentityVerificationAlreadyVerifiedError(error_)
            elif isinstance(error_, IdentityVerificationNotFoundError):
                raise _errors.IdentityVerificationNotFoundError(error_)
            elif isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            elif isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data

    async def send_identity_verification_async(
        self,
        *,
        identity_verification_id: str,
        channel_key: str,
        customer: SendIdentityVerificationBodyCustomer,
        custom_data: Optional[str] = None,
        bypass: Optional[Any] = None,
        operator: IdentityVerificationOperator,
        method: IdentityVerificationMethod,
    ) -> SendIdentityVerificationResponse:
        """본인인증 요청 전송
        
        SMS 또는 APP 방식을 이용하여 본인인증 요청을 전송합니다.
        
        Args:
            identity_verification_id (str): 본인인증 아이디.
            channel_key (str): 채널 키.
            customer (SendIdentityVerificationBodyCustomer): 고객 정보.
            custom_data (Optional[str], optional): 사용자 지정 데이터.
            bypass (Optional[Any], optional): PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고).
            operator (IdentityVerificationOperator): 통신사.
            method (IdentityVerificationMethod): 본인인증 방식.
        
        Returns:
            성공 응답
        
        Raises:
            _errors.ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.IdentityVerificationAlreadySentError: 본인인증 건이 이미 API로 요청된 상태인 경우
            _errors.IdentityVerificationAlreadyVerifiedError: 본인인증 건이 이미 인증 완료된 상태인 경우
            _errors.IdentityVerificationNotFoundError: 요청된 본인인증 건이 존재하지 않는 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = SendIdentityVerificationParam(
            identity_verification_id=identity_verification_id,
        )
        query_ = SendIdentityVerificationQuery()
        body_ = SendIdentityVerificationBody(
            store_id=self.store_id,
            channel_key=channel_key,
            customer=customer,
            custom_data=custom_data,
            bypass=bypass,
            operator=operator,
            method=method,
        )
        response_ = await self.send_async(
            SendIdentityVerificationRequest(param_, query_, body_),
            SendIdentityVerificationResponse,
            SendIdentityVerificationError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ChannelNotFoundError):
                raise _errors.ChannelNotFoundError(error_)
            elif isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            elif isinstance(error_, IdentityVerificationAlreadySentError):
                raise _errors.IdentityVerificationAlreadySentError(error_)
            elif isinstance(error_, IdentityVerificationAlreadyVerifiedError):
                raise _errors.IdentityVerificationAlreadyVerifiedError(error_)
            elif isinstance(error_, IdentityVerificationNotFoundError):
                raise _errors.IdentityVerificationNotFoundError(error_)
            elif isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            elif isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data
