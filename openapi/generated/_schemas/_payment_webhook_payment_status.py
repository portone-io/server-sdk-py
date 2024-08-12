from typing import Literal

type PaymentWebhookPaymentStatus = Literal["READY", "VIRTUAL_ACCOUNT_ISSUED", "PAID", "FAILED", "PARTIAL_CANCELLED", "CANCELLED", "PAY_PENDING"]
"""웹훅 발송 시 결제 건 상태"""

