from portone_server_sdk._openapi._schemas._cancel_amount_exceeds_cancellable_amount_error import (
    CancelAmountExceedsCancellableAmountError,
)
from portone_server_sdk._openapi._schemas._cancel_tax_amount_exceeds_cancellable_tax_amount_error import (
    CancelTaxAmountExceedsCancellableTaxAmountError,
)
from portone_server_sdk._openapi._schemas._cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error import (
    CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError,
)
from portone_server_sdk._openapi._schemas._cancellable_amount_consistency_broken_error import (
    CancellableAmountConsistencyBrokenError,
)
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import (
    InvalidRequestError,
)
from portone_server_sdk._openapi._schemas._payment_already_cancelled_error import (
    PaymentAlreadyCancelledError,
)
from portone_server_sdk._openapi._schemas._payment_not_found_error import (
    PaymentNotFoundError,
)
from portone_server_sdk._openapi._schemas._payment_not_paid_error import (
    PaymentNotPaidError,
)
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._remained_amount_less_than_promotion_min_payment_amount_error import (
    RemainedAmountLessThanPromotionMinPaymentAmountError,
)
from portone_server_sdk._openapi._schemas._sum_of_parts_exceeds_cancel_amount_error import (
    SumOfPartsExceedsCancelAmountError,
)
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

type CancelPaymentError = (
    CancellableAmountConsistencyBrokenError
    | CancelAmountExceedsCancellableAmountError
    | CancelTaxAmountExceedsCancellableTaxAmountError
    | CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError
    | ForbiddenError
    | InvalidRequestError
    | PaymentAlreadyCancelledError
    | PaymentNotFoundError
    | PaymentNotPaidError
    | PgProviderError
    | RemainedAmountLessThanPromotionMinPaymentAmountError
    | SumOfPartsExceedsCancelAmountError
    | UnauthorizedError
)
"""CancelPaymentError"""
