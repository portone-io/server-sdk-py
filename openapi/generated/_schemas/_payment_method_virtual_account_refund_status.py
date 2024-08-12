from typing import Literal

type PaymentMethodVirtualAccountRefundStatus = Literal[
    "PENDING", "PARTIAL_REFUND_FAILED", "FAILED", "COMPLETED"
]
"""가상계좌 환불 상태"""
