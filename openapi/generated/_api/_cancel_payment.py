import dataclasses
from typing import Optional

from portone_server_sdk._api import ApiRequest, ApiErrorResponse
from portone_server_sdk._client import ApiClient
from portone_server_sdk import _errors
from portone_server_sdk._openapi._schemas._cancel_amount_exceeds_cancellable_amount_error import CancelAmountExceedsCancellableAmountError
from portone_server_sdk._openapi._schemas._cancel_payment_body import CancelPaymentBody
from portone_server_sdk._openapi._schemas._cancel_payment_body_refund_account import CancelPaymentBodyRefundAccount
from portone_server_sdk._openapi._schemas._cancel_payment_error import CancelPaymentError
from portone_server_sdk._openapi._schemas._cancel_payment_response import CancelPaymentResponse
from portone_server_sdk._openapi._schemas._cancel_requester import CancelRequester
from portone_server_sdk._openapi._schemas._cancel_tax_amount_exceeds_cancellable_tax_amount_error import CancelTaxAmountExceedsCancellableTaxAmountError
from portone_server_sdk._openapi._schemas._cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error import CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError
from portone_server_sdk._openapi._schemas._cancellable_amount_consistency_broken_error import CancellableAmountConsistencyBrokenError
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import InvalidRequestError
from portone_server_sdk._openapi._schemas._payment_already_cancelled_error import PaymentAlreadyCancelledError
from portone_server_sdk._openapi._schemas._payment_not_found_error import PaymentNotFoundError
from portone_server_sdk._openapi._schemas._payment_not_paid_error import PaymentNotPaidError
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._remained_amount_less_than_promotion_min_payment_amount_error import RemainedAmountLessThanPromotionMinPaymentAmountError
from portone_server_sdk._openapi._schemas._sum_of_parts_exceeds_cancel_amount_error import SumOfPartsExceedsCancelAmountError
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

@dataclasses.dataclass
class CancelPaymentParam:
    payment_id: str = dataclasses.field(metadata={"serde_rename": "paymentId"})
    """결제 건 아이디"""

@dataclasses.dataclass
class CancelPaymentQuery:
    pass

@dataclasses.dataclass
class CancelPaymentRequest(ApiRequest[CancelPaymentResponse, CancelPaymentError, CancelPaymentParam, CancelPaymentQuery, CancelPaymentBody]):
    method = "post"
    path = "/payments/{paymentId}/cancel"

@dataclasses.dataclass
class CancelPayment(ApiClient):
    def cancel_payment(
        self,
        *,
        payment_id: str,
        amount: Optional[int] = None,
        tax_free_amount: Optional[int] = None,
        vat_amount: Optional[int] = None,
        reason: str,
        requester: Optional[CancelRequester] = None,
        current_cancellable_amount: Optional[int] = None,
        refund_account: Optional[CancelPaymentBodyRefundAccount] = None,
    ) -> CancelPaymentResponse:
        """결제 취소
        
        결제 취소를 요청합니다.
        
        Args:
            payment_id (str): 결제 건 아이디.
            amount (Optional[int], optional): 취소 총 금액.
                값을 입력하지 않으면 전액 취소됩니다.
            tax_free_amount (Optional[int], optional): 취소 금액 중 면세 금액.
                값을 입력하지 않으면 전액 과세 취소됩니다.
            vat_amount (Optional[int], optional): 취소 금액 중 부가세액.
                값을 입력하지 않으면 자동 계산됩니다.
            reason (str): 취소 사유.
            requester (Optional[CancelRequester], optional): 취소 요청자.
                고객에 의한 취소일 경우 Customer, 관리자에 의한 취소일 경우 Admin으로 입력합니다.
            current_cancellable_amount (Optional[int], optional): 결제 건의 취소 가능 잔액.
                본 취소 요청 이전의 취소 가능 잔액으로써, 값을 입력하면 잔액이 일치하는 경우에만 취소가 진행됩니다. 값을 입력하지 않으면 별도의 검증 처리를 수행하지 않습니다.
            refund_account (Optional[CancelPaymentBodyRefundAccount], optional): 환불 계좌.
                계좌 환불일 경우 입력합니다. 계좌 환불이 필요한 경우는 가상계좌 환불, 휴대폰 익월 환불 등이 있습니다.
        
        Returns:
            성공 응답
        
        Raises:
            _errors.CancelAmountExceedsCancellableAmountError: 결제 취소 금액이 취소 가능 금액을 초과한 경우
            _errors.CancelTaxAmountExceedsCancellableTaxAmountError: 취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우
            _errors.CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError: 취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우
            _errors.CancellableAmountConsistencyBrokenError: 취소 가능 잔액 검증에 실패한 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PaymentAlreadyCancelledError: 결제가 이미 취소된 경우
            _errors.PaymentNotFoundError: 결제 건이 존재하지 않는 경우
            _errors.PaymentNotPaidError: 결제가 완료되지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.RemainedAmountLessThanPromotionMinPaymentAmountError: 부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우
            _errors.SumOfPartsExceedsCancelAmountError: 면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = CancelPaymentParam(
            payment_id=payment_id,
        )
        query_ = CancelPaymentQuery()
        body_ = CancelPaymentBody(
            store_id=self.store_id,
            amount=amount,
            tax_free_amount=tax_free_amount,
            vat_amount=vat_amount,
            reason=reason,
            requester=requester,
            current_cancellable_amount=current_cancellable_amount,
            refund_account=refund_account,
        )
        response_ = self.send(
            CancelPaymentRequest(param_, query_, body_),
            CancelPaymentResponse,
            CancelPaymentError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, CancelAmountExceedsCancellableAmountError):
                raise _errors.CancelAmountExceedsCancellableAmountError(error_)
            elif isinstance(error_, CancelTaxAmountExceedsCancellableTaxAmountError):
                raise _errors.CancelTaxAmountExceedsCancellableTaxAmountError(error_)
            elif isinstance(error_, CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError):
                raise _errors.CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError(error_)
            elif isinstance(error_, CancellableAmountConsistencyBrokenError):
                raise _errors.CancellableAmountConsistencyBrokenError(error_)
            elif isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            elif isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            elif isinstance(error_, PaymentAlreadyCancelledError):
                raise _errors.PaymentAlreadyCancelledError(error_)
            elif isinstance(error_, PaymentNotFoundError):
                raise _errors.PaymentNotFoundError(error_)
            elif isinstance(error_, PaymentNotPaidError):
                raise _errors.PaymentNotPaidError(error_)
            elif isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            elif isinstance(error_, RemainedAmountLessThanPromotionMinPaymentAmountError):
                raise _errors.RemainedAmountLessThanPromotionMinPaymentAmountError(error_)
            elif isinstance(error_, SumOfPartsExceedsCancelAmountError):
                raise _errors.SumOfPartsExceedsCancelAmountError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data

    async def cancel_payment_async(
        self,
        *,
        payment_id: str,
        amount: Optional[int] = None,
        tax_free_amount: Optional[int] = None,
        vat_amount: Optional[int] = None,
        reason: str,
        requester: Optional[CancelRequester] = None,
        current_cancellable_amount: Optional[int] = None,
        refund_account: Optional[CancelPaymentBodyRefundAccount] = None,
    ) -> CancelPaymentResponse:
        """결제 취소
        
        결제 취소를 요청합니다.
        
        Args:
            payment_id (str): 결제 건 아이디.
            amount (Optional[int], optional): 취소 총 금액.
                값을 입력하지 않으면 전액 취소됩니다.
            tax_free_amount (Optional[int], optional): 취소 금액 중 면세 금액.
                값을 입력하지 않으면 전액 과세 취소됩니다.
            vat_amount (Optional[int], optional): 취소 금액 중 부가세액.
                값을 입력하지 않으면 자동 계산됩니다.
            reason (str): 취소 사유.
            requester (Optional[CancelRequester], optional): 취소 요청자.
                고객에 의한 취소일 경우 Customer, 관리자에 의한 취소일 경우 Admin으로 입력합니다.
            current_cancellable_amount (Optional[int], optional): 결제 건의 취소 가능 잔액.
                본 취소 요청 이전의 취소 가능 잔액으로써, 값을 입력하면 잔액이 일치하는 경우에만 취소가 진행됩니다. 값을 입력하지 않으면 별도의 검증 처리를 수행하지 않습니다.
            refund_account (Optional[CancelPaymentBodyRefundAccount], optional): 환불 계좌.
                계좌 환불일 경우 입력합니다. 계좌 환불이 필요한 경우는 가상계좌 환불, 휴대폰 익월 환불 등이 있습니다.
        
        Returns:
            성공 응답
        
        Raises:
            _errors.CancelAmountExceedsCancellableAmountError: 결제 취소 금액이 취소 가능 금액을 초과한 경우
            _errors.CancelTaxAmountExceedsCancellableTaxAmountError: 취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우
            _errors.CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError: 취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우
            _errors.CancellableAmountConsistencyBrokenError: 취소 가능 잔액 검증에 실패한 경우
            _errors.ForbiddenError: 요청이 거절된 경우
            _errors.InvalidRequestError: 요청된 입력 정보가 유효하지 않은 경우
            _errors.PaymentAlreadyCancelledError: 결제가 이미 취소된 경우
            _errors.PaymentNotFoundError: 결제 건이 존재하지 않는 경우
            _errors.PaymentNotPaidError: 결제가 완료되지 않은 경우
            _errors.PgProviderError: PG사에서 오류를 전달한 경우
            _errors.RemainedAmountLessThanPromotionMinPaymentAmountError: 부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우
            _errors.SumOfPartsExceedsCancelAmountError: 면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우
            _errors.UnauthorizedError: 인증 정보가 올바르지 않은 경우
        """
        param_ = CancelPaymentParam(
            payment_id=payment_id,
        )
        query_ = CancelPaymentQuery()
        body_ = CancelPaymentBody(
            store_id=self.store_id,
            amount=amount,
            tax_free_amount=tax_free_amount,
            vat_amount=vat_amount,
            reason=reason,
            requester=requester,
            current_cancellable_amount=current_cancellable_amount,
            refund_account=refund_account,
        )
        response_ = await self.send_async(
            CancelPaymentRequest(param_, query_, body_),
            CancelPaymentResponse,
            CancelPaymentError,
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
            if isinstance(error_, CancelAmountExceedsCancellableAmountError):
                raise _errors.CancelAmountExceedsCancellableAmountError(error_)
            elif isinstance(error_, CancelTaxAmountExceedsCancellableTaxAmountError):
                raise _errors.CancelTaxAmountExceedsCancellableTaxAmountError(error_)
            elif isinstance(error_, CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError):
                raise _errors.CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError(error_)
            elif isinstance(error_, CancellableAmountConsistencyBrokenError):
                raise _errors.CancellableAmountConsistencyBrokenError(error_)
            elif isinstance(error_, ForbiddenError):
                raise _errors.ForbiddenError(error_)
            elif isinstance(error_, InvalidRequestError):
                raise _errors.InvalidRequestError(error_)
            elif isinstance(error_, PaymentAlreadyCancelledError):
                raise _errors.PaymentAlreadyCancelledError(error_)
            elif isinstance(error_, PaymentNotFoundError):
                raise _errors.PaymentNotFoundError(error_)
            elif isinstance(error_, PaymentNotPaidError):
                raise _errors.PaymentNotPaidError(error_)
            elif isinstance(error_, PgProviderError):
                raise _errors.PgProviderError(error_)
            elif isinstance(error_, RemainedAmountLessThanPromotionMinPaymentAmountError):
                raise _errors.RemainedAmountLessThanPromotionMinPaymentAmountError(error_)
            elif isinstance(error_, SumOfPartsExceedsCancelAmountError):
                raise _errors.SumOfPartsExceedsCancelAmountError(error_)
            else:
                raise _errors.UnauthorizedError(error_)
        else:
            return response_.data
