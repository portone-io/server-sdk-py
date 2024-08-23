import dataclasses
from typing import Any, Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._async import ApiClient
from portone_server_sdk._openapi._schemas._channel_not_found_error import ChannelNotFoundError
from portone_server_sdk._openapi._schemas._channel_specific_error import ChannelSpecificError
from portone_server_sdk._openapi._schemas._customer_input import CustomerInput
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._instant_billing_key_payment_method_input import InstantBillingKeyPaymentMethodInput
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._issue_billing_key_body import IssueBillingKeyBody
from portone_server_sdk._openapi._schemas._issue_billing_key_error import IssueBillingKeyError
from portone_server_sdk._openapi._schemas._issue_billing_key_response import IssueBillingKeyResponse
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class IssueBillingKeyParam:
    pass

@dataclasses.dataclass
class IssueBillingKeyQuery:
    pass

@dataclasses.dataclass
class IssueBillingKeyRequest(ApiRequest[IssueBillingKeyResponse, IssueBillingKeyError, IssueBillingKeyParam, IssueBillingKeyQuery, IssueBillingKeyBody]):
    method = "post"
    path = "/billing-keys"

@dataclasses.dataclass
class IssueBillingKey(ApiClient):
    async def issue_billing_key(
        self,
        storeId: Optional[str],
        method: InstantBillingKeyPaymentMethodInput,
        channelKey: Optional[str],
        channelGroupId: Optional[str],
        customer: Optional[CustomerInput],
        customData: Optional[str],
        bypass: Optional[Any],
        noticeUrls: Optional[list[str]],
    ) -> IssueBillingKeyResponse:
        """빌링키 발급
        
        빌링키 발급을 요청합니다.
        
        Args:
            storeId (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
            method (InstantBillingKeyPaymentMethodInput): 빌링키 결제 수단 정보.
            channelKey (Optional[str]): 채널 키.
                채널 키 또는 채널 그룹 ID 필수
            channelGroupId (Optional[str]): 채널 그룹 ID.
                채널 키 또는 채널 그룹 ID 필수
            customer (Optional[CustomerInput]): 고객 정보.
            customData (Optional[str]): 사용자 지정 데이터.
            bypass (Optional[Any]): PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고).
            noticeUrls (Optional[list[str]]): 웹훅 주소.
                빌링키 발급 시 요청을 받을 웹훅 주소입니다.
                상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
                입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
        
        Returns:
            IssueBillingKeyResponse: 성공 응답
        
        Raises:
            _errors.ChannelNotFoundError: 요청된 채널이 존재하지 않는 경우
            _errors.ChannelSpecificError: 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = IssueBillingKeyParam()
        query_ = IssueBillingKeyQuery()
        body_ = IssueBillingKeyBody(
            storeId=storeId,
            method=method,
            channelKey=channelKey,
            channelGroupId=channelGroupId,
            customer=customer,
            customData=customData,
            bypass=bypass,
            noticeUrls=noticeUrls,
        )
        response_ = await self.send(
            IssueBillingKeyRequest(param_, query_, body_),
            IssueBillingKeyResponse,
            IssueBillingKeyError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ChannelNotFoundError):
                raise _errors.ChannelNotFoundError(error_)
            if isinstance(error_, ChannelSpecificError):
                raise _errors.ChannelSpecificError(error_)
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
