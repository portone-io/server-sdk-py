from portone_server_sdk._openapi._schemas._already_paid_error import AlreadyPaidError
from portone_server_sdk._openapi._schemas._channel_not_found_error import (
    ChannelNotFoundError,
)
from portone_server_sdk._openapi._schemas._discount_amount_exceeds_total_amount_error import (
    DiscountAmountExceedsTotalAmountError,
)
from portone_server_sdk._openapi._schemas._forbidden_error import ForbiddenError
from portone_server_sdk._openapi._schemas._invalid_request_error import (
    InvalidRequestError,
)
from portone_server_sdk._openapi._schemas._pg_provider_error import PgProviderError
from portone_server_sdk._openapi._schemas._promotion_pay_method_does_not_match_error import (
    PromotionPayMethodDoesNotMatchError,
)
from portone_server_sdk._openapi._schemas._sum_of_parts_exceeds_total_amount_error import (
    SumOfPartsExceedsTotalAmountError,
)
from portone_server_sdk._openapi._schemas._unauthorized_error import UnauthorizedError

type PayInstantlyError = (
    AlreadyPaidError
    | ChannelNotFoundError
    | DiscountAmountExceedsTotalAmountError
    | ForbiddenError
    | InvalidRequestError
    | PgProviderError
    | PromotionPayMethodDoesNotMatchError
    | SumOfPartsExceedsTotalAmountError
    | UnauthorizedError
)
"""PayInstantlyError"""
