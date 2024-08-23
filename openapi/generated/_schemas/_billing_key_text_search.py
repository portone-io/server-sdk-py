import dataclasses
from portone_server_sdk._openapi._schemas._billing_key_text_search_field import BillingKeyTextSearchField

@dataclasses.dataclass
class BillingKeyTextSearch:
    """통합검색 입력 정보"""
    field: BillingKeyTextSearchField
    value: str

