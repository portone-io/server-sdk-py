import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._get_payment_schedules_body import GetPaymentSchedulesBody
from portone_server_sdk._openapi._schemas._get_payment_schedules_error import GetPaymentSchedulesError
from portone_server_sdk._openapi._schemas._get_payment_schedules_response import GetPaymentSchedulesResponse
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._page_input import PageInput
from portone_server_sdk._openapi._schemas._payment_schedule_filter_input import PaymentScheduleFilterInput
from portone_server_sdk._openapi._schemas._payment_schedule_sort_input import PaymentScheduleSortInput
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class GetPaymentSchedulesParam:
    pass

@dataclasses.dataclass
class GetPaymentSchedulesQuery:
    pass

@dataclasses.dataclass
class GetPaymentSchedulesRequest(ApiRequest[GetPaymentSchedulesResponse, GetPaymentSchedulesError, GetPaymentSchedulesParam, GetPaymentSchedulesQuery, GetPaymentSchedulesBody]):
    method = "get"
    path = "/payment-schedules"

@dataclasses.dataclass
class GetPaymentSchedules(ApiClient):
    def get_payment_schedules(
        self,
        page: Optional[PageInput],
        sort: Optional[PaymentScheduleSortInput],
        filter: Optional[PaymentScheduleFilterInput],
    ) -> GetPaymentSchedulesResponse:
        """결제 예약 다건 조회
        
        주어진 조건에 맞는 결제 예약 건들을 조회합니다.
        `filter.from`, `filter.until` 파라미터의 기본값이 결제 시점 기준 지난 90일에 속하는 건을 조회하도록 되어 있으니, 미래 예약 상태의 건을 조회하기 위해서는 해당 파라미터를 직접 설정해 주셔야 합니다.
        
        Args:
            page (Optional[PageInput]): 요청할 페이지 정보.
                미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
            sort (Optional[PaymentScheduleSortInput]): 정렬 조건.
                미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
            filter (Optional[PaymentScheduleFilterInput]): 조회할 결제 예약 건의 조건 필터.
        
        Returns:
            GetPaymentSchedulesResponse: 성공 응답으로 조회된 예약 결제 건 리스트가 반환됩니다.
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = GetPaymentSchedulesParam()
        query_ = GetPaymentSchedulesQuery()
        body_ = GetPaymentSchedulesBody(
            page=page,
            sort=sort,
            filter=filter,
        )
        response_ = self.send(
            GetPaymentSchedulesRequest(param_, query_, body_),
            GetPaymentSchedulesResponse,
            GetPaymentSchedulesError,
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
