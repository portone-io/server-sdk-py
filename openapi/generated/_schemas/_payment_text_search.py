import dataclasses
from portone_server_sdk._openapi._schemas._payment_text_search_field import (
    PaymentTextSearchField,
)


@dataclasses.dataclass(kw_only=True)
class PaymentTextSearch:
    """통합검색 입력 정보"""

    field: PaymentTextSearchField
    value: str
