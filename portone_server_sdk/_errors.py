from dataclasses import InitVar, dataclass, field

from ._openapi import _schemas


@dataclass(init=False)
class PortOneError(Exception):
    """포트원 SDK에서 발생하는 모든 에러의 기본 타입입니다."""

    message: str


@dataclass(slots=True)
class ForbiddenError(PortOneError):
    """요청이 거절된 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.ForbiddenError]

    def __post_init__(self, error: _schemas.ForbiddenError) -> None:
        self.message = (
            "요청이 거절되었습니다." if error.message is None else error.message
        )


@dataclass(slots=True)
class InvalidRequestError(PortOneError):
    """요청된 입력 정보가 유효하지 않은 경우

    허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
    """

    message: str = field(init=False)
    error: InitVar[_schemas.InvalidRequestError]

    def __post_init__(self, error: _schemas.InvalidRequestError) -> None:
        self.message = (
            "요청된 입력 정보가 유효하지 않습니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class PaymentNotFoundError(PortOneError):
    """결제 건이 존재하지 않는 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.PaymentNotFoundError]

    def __post_init__(self, error: _schemas.PaymentNotFoundError) -> None:
        self.message = (
            "결제 건이 존재하지 않습니다." if error.message is None else error.message
        )


@dataclass(slots=True)
class PaymentNotPaidError(PortOneError):
    """결제가 완료되지 않은 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.PaymentNotPaidError]

    def __post_init__(self, error: _schemas.PaymentNotPaidError) -> None:
        self.message = (
            "결제가 완료되지 않았습니다." if error.message is None else error.message
        )


@dataclass(slots=True)
class PgProviderError(PortOneError):
    """PG사에서 오류를 전달한 경우"""

    message: str = field(init=False)
    pgCode: str = field(init=False)
    pgMessage: str = field(init=False)
    error: InitVar[_schemas.PgProviderError]

    def __post_init__(self, error: _schemas.PgProviderError) -> None:
        self.message = (
            "PG사에서 오류를 전달했습니다." if error.message is None else error.message
        )
        self.pgCode = error.pgCode
        self.pgMessage = error.pgMessage


@dataclass(slots=True)
class UnauthorizedError(PortOneError):
    """인증 정보가 올바르지 않은 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.UnauthorizedError]

    def __post_init__(self, error: _schemas.UnauthorizedError) -> None:
        self.message = (
            "인증 정보가 올바르지 않습니다." if error.message is None else error.message
        )


@dataclass(slots=True)
class WebhookNotFoundError(PortOneError):
    """웹훅 내역이 존재하지 않는 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.WebhookNotFoundError]

    def __post_init__(self, error: _schemas.WebhookNotFoundError) -> None:
        self.message = (
            "웹훅 내역이 존재하지 않습니다." if error.message is None else error.message
        )


@dataclass(slots=True)
class AlreadyPaidError(PortOneError):
    """결제가 이미 완료된 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.AlreadyPaidError]

    def __post_init__(self, error: _schemas.AlreadyPaidError) -> None:
        self.message = (
            "결제가 이미 완료되었습니다." if error.message is None else error.message
        )


@dataclass(slots=True)
class BillingKeyAlreadyDeletedError(PortOneError):
    """빌링키가 이미 삭제된 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.BillingKeyAlreadyDeletedError]

    def __post_init__(self, error: _schemas.BillingKeyAlreadyDeletedError) -> None:
        self.message = (
            "빌링키가 이미 삭제되었습니다." if error.message is None else error.message
        )


@dataclass(slots=True)
class BillingKeyNotFoundError(PortOneError):
    """빌링키가 존재하지 않는 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.BillingKeyNotFoundError]

    def __post_init__(self, error: _schemas.BillingKeyNotFoundError) -> None:
        self.message = (
            "빌링키가 존재하지 않습니다." if error.message is None else error.message
        )


@dataclass(slots=True)
class ChannelNotFoundError(PortOneError):
    """요청된 채널이 존재하지 않는 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.ChannelNotFoundError]

    def __post_init__(self, error: _schemas.ChannelNotFoundError) -> None:
        self.message = (
            "요청된 채널이 존재하지 않습니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class DiscountAmountExceedsTotalAmountError(PortOneError):
    """프로모션 할인 금액이 결제 시도 금액 이상인 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.DiscountAmountExceedsTotalAmountError]

    def __post_init__(
        self, error: _schemas.DiscountAmountExceedsTotalAmountError
    ) -> None:
        self.message = (
            "프로모션 할인 금액이 결제 시도 금액 이상입니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class PromotionPayMethodDoesNotMatchError(PortOneError):
    """결제수단이 프로모션에 지정된 것과 일치하지 않는 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.PromotionPayMethodDoesNotMatchError]

    def __post_init__(
        self, error: _schemas.PromotionPayMethodDoesNotMatchError
    ) -> None:
        self.message = (
            "결제수단이 프로모션에 지정된 것과 일치하지 않습니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class SumOfPartsExceedsTotalAmountError(PortOneError):
    """면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.SumOfPartsExceedsTotalAmountError]

    def __post_init__(self, error: _schemas.SumOfPartsExceedsTotalAmountError) -> None:
        self.message = (
            "하위 항목들의 합이 전체 결제 금액을 초과했습니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class CashReceiptNotFoundError(PortOneError):
    """현금영수증이 존재하지 않는 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.CashReceiptNotFoundError]

    def __post_init__(self, error: _schemas.CashReceiptNotFoundError) -> None:
        self.message = (
            "현금영수증이 존재하지 않습니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class AlreadyPaidOrWaitingError(PortOneError):
    """결제가 이미 완료되었거나 대기중인 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.AlreadyPaidOrWaitingError]

    def __post_init__(self, error: _schemas.AlreadyPaidOrWaitingError) -> None:
        self.message = (
            "결제가 이미 완료되었거나 대기중입니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class PaymentScheduleAlreadyExistsError(PortOneError):
    """결제 예약건이 이미 존재하는 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.PaymentScheduleAlreadyExistsError]

    def __post_init__(self, error: _schemas.PaymentScheduleAlreadyExistsError) -> None:
        self.message = (
            "결제 예약건이 이미 존재합니다." if error.message is None else error.message
        )


@dataclass(slots=True)
class PaymentNotWaitingForDepositError(PortOneError):
    """결제 건이 입금 대기 상태가 아닌 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.PaymentNotWaitingForDepositError]

    def __post_init__(self, error: _schemas.PaymentNotWaitingForDepositError) -> None:
        self.message = (
            "결제 건이 입금 대기 상태가 아닙니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class CancelAmountExceedsCancellableAmountError(PortOneError):
    """결제 취소 금액이 취소 가능 금액을 초과한 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.CancelAmountExceedsCancellableAmountError]

    def __post_init__(
        self, error: _schemas.CancelAmountExceedsCancellableAmountError
    ) -> None:
        self.message = (
            "결제 취소 금액이 취소 가능 금액을 초과했습니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class CancelTaxAmountExceedsCancellableTaxAmountError(PortOneError):
    """취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.CancelTaxAmountExceedsCancellableTaxAmountError]

    def __post_init__(
        self, error: _schemas.CancelTaxAmountExceedsCancellableTaxAmountError
    ) -> None:
        self.message = (
            "취소 과세 금액이 취소 가능한 과세 금액을 초과했습니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError(PortOneError):
    """취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError]

    def __post_init__(
        self, error: _schemas.CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError
    ) -> None:
        self.message = (
            "취소 면세 금액이 취소 가능한 면세 금액을 초과했습니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class PaymentAlreadyCancelledError(PortOneError):
    """결제가 이미 취소된 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.PaymentAlreadyCancelledError]

    def __post_init__(self, error: _schemas.PaymentAlreadyCancelledError) -> None:
        self.message = (
            "결제가 이미 취소되었습니다." if error.message is None else error.message
        )


@dataclass(slots=True)
class RemainedAmountLessThanPromotionMinPaymentAmountError(PortOneError):
    """부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.RemainedAmountLessThanPromotionMinPaymentAmountError]

    def __post_init__(
        self, error: _schemas.RemainedAmountLessThanPromotionMinPaymentAmountError
    ) -> None:
        self.message = (
            "취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아집니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class SumOfPartsExceedsCancelAmountError(PortOneError):
    """면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.SumOfPartsExceedsCancelAmountError]

    def __post_init__(self, error: _schemas.SumOfPartsExceedsCancelAmountError) -> None:
        self.message = (
            "하위 항목들의 합이 전체 취소 금액을 초과했습니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class CashReceiptNotIssuedError(PortOneError):
    """현금영수증이 발급되지 않은 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.CashReceiptNotIssuedError]

    def __post_init__(self, error: _schemas.CashReceiptNotIssuedError) -> None:
        self.message = (
            "현금영수증이 발급되지 않았습니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class CancellableAmountConsistencyBrokenError(PortOneError):
    """취소 가능 잔액 검증에 실패한 경우"""

    message: str = field(init=False)
    error: InitVar[_schemas.CancellableAmountConsistencyBrokenError]

    def __post_init__(
        self, error: _schemas.CancellableAmountConsistencyBrokenError
    ) -> None:
        self.message = (
            "취소 가능 잔액 검증에 실패했습니다."
            if error.message is None
            else error.message
        )


@dataclass(slots=True)
class UnknownError(PortOneError):
    """알 수 없는 경우"""

    message: str = field(default="알 수 없는 오류가 발생했습니다.", init=False)
    error: object
