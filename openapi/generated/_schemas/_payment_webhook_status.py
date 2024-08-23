from typing import Literal

PaymentWebhookStatus = Literal["SUCCEEDED", "FAILED_NOT_OK_RESPONSE", "FAILED_UNEXPECTED_ERROR"]
"""웹훅 전송 상태"""

