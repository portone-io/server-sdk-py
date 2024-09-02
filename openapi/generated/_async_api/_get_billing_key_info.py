import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse, Empty
from portone_server_sdk import _errors
from portone_server_sdk._async import ApiClient
from portone_server_sdk._openapi._schemas._billing_key_info import BillingKeyInfo
from portone_server_sdk._openapi._schemas._billing_key_not_found_error import BillingKeyNotFoundError
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._get_billing_key_info_error import GetBillingKeyInfoError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class GetBillingKeyInfoParam:
    billing_key: str = dataclasses.field(metadata={"serde_rename": "billingKey"})
    """조회할 빌링키"""

@dataclasses.dataclass
class GetBillingKeyInfoQuery:
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId", "serde_skip_if": lambda value: value is None})
    """상점 아이디
    
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """

@dataclasses.dataclass
class GetBillingKeyInfoRequest(ApiRequest[BillingKeyInfo, GetBillingKeyInfoError, GetBillingKeyInfoParam, GetBillingKeyInfoQuery, Empty]):
    method = "get"
    path = "/billing-keys/{billingKey}"

@dataclasses.dataclass
class GetBillingKeyInfo(ApiClient):
    async def get_billing_key_info(
        self,
        *,
        billing_key: str,
    ) -> BillingKeyInfo:
        """빌링키 단건 조회
        
        주어진 빌링키에 대응되는 빌링키 정보를 조회합니다.
        
        Args:
            billing_key (str): 조회할 빌링키.
        
        Returns:
            성공 응답으로 빌링키 정보를 반환합니다.
        
        Raises:
            _errors.BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = GetBillingKeyInfoParam(
            billing_key=billing_key,
        )
        query_ = GetBillingKeyInfoQuery(
            store_id=self.store_id,
        )
        body_ = Empty()
        response_ = await self.send(
            GetBillingKeyInfoRequest(param_, query_, body_),
            BillingKeyInfo,
            GetBillingKeyInfoError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, BillingKeyNotFoundError):
                raise _errors.BillingKeyNotFoundError(error_)
            elif isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            elif isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data
