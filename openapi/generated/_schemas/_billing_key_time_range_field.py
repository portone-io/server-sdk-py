from typing import Literal

BillingKeyTimeRangeField = Literal["REQUESTED_AT", "ISSUED_AT", "DELETED_AT", "STATUS_TIMESTAMP"]
"""빌링키 다건 조회 시, 시각 범위를 적용할 필드"""

