from typing import Literal

PaymentStatus = Literal["READY", "PENDING", "VIRTUAL_ACCOUNT_ISSUED", "PAID", "FAILED", "PARTIAL_CANCELLED", "CANCELLED"]
"""결제 건 상태"""

