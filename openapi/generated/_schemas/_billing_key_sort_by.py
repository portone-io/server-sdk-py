from typing import Literal

type BillingKeySortBy = Literal[
    "REQUESTED_AT", "ISSUED_AT", "DELETED_AT", "STATUS_TIMESTAMP"
]
"""빌링키 정렬 기준"""