import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse, Empty
from portone_server_sdk import _errors
from portone_server_sdk._sync import ApiClient
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._get_payment_error import GetPaymentError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._payment import Payment
from portone_server_sdk._openapi._schemas._payment_not_found_error import PaymentNotFoundError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class GetPaymentParam:
    paymentId: str
    """조회할 결제 아이디"""

@dataclasses.dataclass
class GetPaymentQuery:
    storeId: Optional[str]
    """상점 아이디"""

@dataclasses.dataclass
class GetPaymentRequest(ApiRequest[Payment, GetPaymentError, GetPaymentParam, GetPaymentQuery, Empty]):
    method = "get"
    path = "/payments/{paymentId}"

@dataclasses.dataclass
class GetPayment(ApiClient):
    def get_payment(
        self,
        paymentId: str,
        storeId: Optional[str],
    ) -> Payment:
        """결제 단건 조회
        
        주어진 아이디에 대응되는 결제 건을 조회합니다.
        
        Args:
            paymentId (str): 조회할 결제 아이디.
            storeId (Optional[str]): 상점 아이디.
        
        Returns:
            Payment: 성공 응답으로 결제 건 객체를 반환합니다.
        
        Raises:
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PaymentNotFoundError: 결제 건이 존재하지 않는 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = GetPaymentParam(
            paymentId=paymentId,
        )
        query_ = GetPaymentQuery(
            storeId=storeId,
        )
        body_ = Empty()
        response_ = self.send(
            GetPaymentRequest(param_, query_, body_),
            Payment,
            GetPaymentError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            if isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            if isinstance(error_, PaymentNotFoundError):
                raise _errors.PaymentNotFoundError(error_)
            if isinstance(error_, UnauthorizedError):
                raise _errors.UnauthorizedError(error_)

        return response_.data
