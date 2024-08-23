import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse, Empty
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._get_payment_schedule_error import GetPaymentScheduleError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._payment_schedule import PaymentSchedule
from portone_server_sdk._openapi._schemas._payment_schedule_not_found_error import PaymentScheduleNotFoundError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class GetPaymentScheduleParam:
    paymentScheduleId: str
    """조회할 결제 예약 건 아이디"""

@dataclasses.dataclass
class GetPaymentScheduleQuery:
    storeId: Optional[str]
    """상점 아이디
    
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """

@dataclasses.dataclass
class GetPaymentScheduleRequest(ApiRequest[PaymentSchedule, GetPaymentScheduleError, GetPaymentScheduleParam, GetPaymentScheduleQuery, Empty]):
    method = "get"
    path = "/payment-schedules/{paymentScheduleId}"

@dataclasses.dataclass
class GetPaymentSchedule(ApiClient):
    def get_payment_schedule(
        self,
        paymentScheduleId: str,
        storeId: Optional[str],
    ) -> PaymentSchedule:
        """결제 예약 단건 조회
        
        주어진 아이디에 대응되는 결제 예약 건을 조회합니다.
        
        Args:
            paymentScheduleId (str): 조회할 결제 예약 건 아이디.
            storeId (Optional[str]): 상점 아이디.
                접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
        
        Returns:
            PaymentSchedule: 성공 응답으로 결제 예약 건 객체를 반환합니다.
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PaymentScheduleNotFoundError: 결제 예약건이 존재하지 않는 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = GetPaymentScheduleParam(
            paymentScheduleId=paymentScheduleId,
        )
        query_ = GetPaymentScheduleQuery(
            storeId=storeId,
        )
        body_ = Empty()
        response_ = self.send(
            GetPaymentScheduleRequest(param_, query_, body_),
            PaymentSchedule,
            GetPaymentScheduleError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, PaymentScheduleNotFoundError):
                raise _errors.PaymentScheduleNotFoundError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
