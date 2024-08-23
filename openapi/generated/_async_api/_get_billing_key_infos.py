import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._async import ApiClient
from portone_server_sdk._openapi._schemas._billing_key_filter_input import BillingKeyFilterInput
from portone_server_sdk._openapi._schemas._billing_key_sort_input import BillingKeySortInput
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._get_billing_key_infos_body import GetBillingKeyInfosBody
from portone_server_sdk._openapi._schemas._get_billing_key_infos_error import GetBillingKeyInfosError
from portone_server_sdk._openapi._schemas._get_billing_key_infos_response import GetBillingKeyInfosResponse
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._page_input import PageInput
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class GetBillingKeyInfosParam:
    pass

@dataclasses.dataclass
class GetBillingKeyInfosQuery:
    pass

@dataclasses.dataclass
class GetBillingKeyInfosRequest(ApiRequest[GetBillingKeyInfosResponse, GetBillingKeyInfosError, GetBillingKeyInfosParam, GetBillingKeyInfosQuery, GetBillingKeyInfosBody]):
    method = "get"
    path = "/billing-keys"

@dataclasses.dataclass
class GetBillingKeyInfos(ApiClient):
    async def get_billing_key_infos(
        self,
        page: Optional[PageInput],
        sort: Optional[BillingKeySortInput],
        filter: Optional[BillingKeyFilterInput],
    ) -> GetBillingKeyInfosResponse:
        """빌링키 다건 조회
        
        주어진 조건에 맞는 빌링키들을 페이지 기반으로 조회합니다.
        
        Args:
            page (Optional[PageInput]): 요청할 페이지 정보.
                미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
            sort (Optional[BillingKeySortInput]): 정렬 조건.
                미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
            filter (Optional[BillingKeyFilterInput]): 조회할 빌링키 조건 필터.
                V1 빌링키 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
        
        Returns:
            GetBillingKeyInfosResponse: 성공 응답으로 조회된 빌링키 리스트와 페이지 정보가 반환됩니다.
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = GetBillingKeyInfosParam()
        query_ = GetBillingKeyInfosQuery()
        body_ = GetBillingKeyInfosBody(
            page=page,
            sort=sort,
            filter=filter,
        )
        response_ = await self.send(
            GetBillingKeyInfosRequest(param_, query_, body_),
            GetBillingKeyInfosResponse,
            GetBillingKeyInfosError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
