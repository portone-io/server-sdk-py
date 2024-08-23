import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._async import ApiClient
from portone_server_sdk._openapi._schemas._billing_key_already_deleted_error import BillingKeyAlreadyDeletedError
from portone_server_sdk._openapi._schemas._billing_key_not_found_error import BillingKeyNotFoundError
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._payment_schedule_already_processed_error import PaymentScheduleAlreadyProcessedError
from portone_server_sdk._openapi._schemas._payment_schedule_already_revoked_error import PaymentScheduleAlreadyRevokedError
from portone_server_sdk._openapi._schemas._payment_schedule_not_found_error import PaymentScheduleNotFoundError
from portone_server_sdk._openapi._schemas._revoke_payment_schedules_body import RevokePaymentSchedulesBody
from portone_server_sdk._openapi._schemas._revoke_payment_schedules_error import RevokePaymentSchedulesError
from portone_server_sdk._openapi._schemas._revoke_payment_schedules_response import RevokePaymentSchedulesResponse
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class RevokePaymentSchedulesParam:
    pass

@dataclasses.dataclass
class RevokePaymentSchedulesQuery:
    pass

@dataclasses.dataclass
class RevokePaymentSchedulesRequest(ApiRequest[RevokePaymentSchedulesResponse, RevokePaymentSchedulesError, RevokePaymentSchedulesParam, RevokePaymentSchedulesQuery, RevokePaymentSchedulesBody]):
    method = "delete"
    path = "/payment-schedules"

@dataclasses.dataclass
class RevokePaymentSchedules(ApiClient):
    async def revoke_payment_schedules(
        self,
        storeId: Optional[str],
        billingKey: Optional[str],
        scheduleIds: Optional[list[str]],
    ) -> RevokePaymentSchedulesResponse:
        """결제 예약 취소
        
        결제 예약 건을 취소합니다.
        
        Args:
            storeId (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
            billingKey (Optional[str]): 빌링키.
            scheduleIds (Optional[list[str]]): 결제 예약 건 아이디 목록.
        
        Returns:
            RevokePaymentSchedulesResponse: 성공 응답
        
        Raises:
            _errors.BillingKeyAlreadyDeletedError: 빌링키가 이미 삭제된 경우
            _errors.BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PaymentScheduleAlreadyProcessedError: 결제 예약건이 이미 처리된 경우
            _errors.PaymentScheduleAlreadyRevokedError: 결제 예약건이 이미 취소된 경우
            _errors.PaymentScheduleNotFoundError: 결제 예약건이 존재하지 않는 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = RevokePaymentSchedulesParam()
        query_ = RevokePaymentSchedulesQuery()
        body_ = RevokePaymentSchedulesBody(
            storeId=storeId,
            billingKey=billingKey,
            scheduleIds=scheduleIds,
        )
        response_ = await self.send(
            RevokePaymentSchedulesRequest(param_, query_, body_),
            RevokePaymentSchedulesResponse,
            RevokePaymentSchedulesError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, BillingKeyAlreadyDeletedError):
                raise _errors.BillingKeyAlreadyDeletedError(error_)
            if isinstance(error_, BillingKeyNotFoundError):
                raise _errors.BillingKeyNotFoundError(error_)
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, PaymentScheduleAlreadyProcessedError):
                raise _errors.PaymentScheduleAlreadyProcessedError(error_)
            if isinstance(error_, PaymentScheduleAlreadyRevokedError):
                raise _errors.PaymentScheduleAlreadyRevokedError(error_)
            if isinstance(error_, PaymentScheduleNotFoundError):
                raise _errors.PaymentScheduleNotFoundError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
