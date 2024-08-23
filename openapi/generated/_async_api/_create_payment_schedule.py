import dataclasses

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk import _errors
from portone_server_sdk._async import ApiClient
from portone_server_sdk._openapi._schemas._already_paid_or_waiting_error import AlreadyPaidOrWaitingError
from portone_server_sdk._openapi._schemas._billing_key_already_deleted_error import BillingKeyAlreadyDeletedError
from portone_server_sdk._openapi._schemas._billing_key_not_found_error import BillingKeyNotFoundError
from portone_server_sdk._openapi._schemas._billing_key_payment_input import BillingKeyPaymentInput
from portone_server_sdk._openapi._schemas._create_payment_schedule_body import CreatePaymentScheduleBody
from portone_server_sdk._openapi._schemas._create_payment_schedule_error import CreatePaymentScheduleError
from portone_server_sdk._openapi._schemas._create_payment_schedule_response import CreatePaymentScheduleResponse
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._payment_schedule_already_exists_error import PaymentScheduleAlreadyExistsError
from portone_server_sdk._openapi._schemas._sum_of_parts_exceeds_total_amount_error import SumOfPartsExceedsTotalAmountError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class CreatePaymentScheduleParam:
    paymentId: str
    """결제 건 아이디"""

@dataclasses.dataclass
class CreatePaymentScheduleQuery:
    pass

@dataclasses.dataclass
class CreatePaymentScheduleRequest(ApiRequest[CreatePaymentScheduleResponse, CreatePaymentScheduleError, CreatePaymentScheduleParam, CreatePaymentScheduleQuery, CreatePaymentScheduleBody]):
    method = "post"
    path = "/payments/{paymentId}/schedule"

@dataclasses.dataclass
class CreatePaymentSchedule(ApiClient):
    async def create_payment_schedule(
        self,
        paymentId: str,
        payment: BillingKeyPaymentInput,
        timeToPay: str,
    ) -> CreatePaymentScheduleResponse:
        """결제 예약
        
        결제를 예약합니다.
        
        Args:
            paymentId (str): 결제 건 아이디.
            payment (BillingKeyPaymentInput): 빌링키 결제 입력 정보.
            timeToPay (str): 결제 예정 시점.
        
        Returns:
            CreatePaymentScheduleResponse: 성공 응답
        
        Raises:
            _errors.AlreadyPaidOrWaitingError: 결제가 이미 완료되었거나 대기중인 경우
            _errors.BillingKeyAlreadyDeletedError: 빌링키가 이미 삭제된 경우
            _errors.BillingKeyNotFoundError: 빌링키가 존재하지 않는 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PaymentScheduleAlreadyExistsError: 결제 예약건이 이미 존재하는 경우
            _errors.SumOfPartsExceedsTotalAmountError: 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = CreatePaymentScheduleParam(
            paymentId=paymentId,
        )
        query_ = CreatePaymentScheduleQuery()
        body_ = CreatePaymentScheduleBody(
            payment=payment,
            timeToPay=timeToPay,
        )
        response_ = await self.send(
            CreatePaymentScheduleRequest(param_, query_, body_),
            CreatePaymentScheduleResponse,
            CreatePaymentScheduleError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, AlreadyPaidOrWaitingError):
                raise _errors.AlreadyPaidOrWaitingError(error_)
            if isinstance(error_, BillingKeyAlreadyDeletedError):
                raise _errors.BillingKeyAlreadyDeletedError(error_)
            if isinstance(error_, BillingKeyNotFoundError):
                raise _errors.BillingKeyNotFoundError(error_)
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, PaymentScheduleAlreadyExistsError):
                raise _errors.PaymentScheduleAlreadyExistsError(error_)
            if isinstance(error_, SumOfPartsExceedsTotalAmountError):
                raise _errors.SumOfPartsExceedsTotalAmountError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
