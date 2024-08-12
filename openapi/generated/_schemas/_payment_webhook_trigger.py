from typing import Literal

type PaymentWebhookTrigger = Literal["MANUAL", "VIRTUAL_ACCOUNT_DEPOSIT", "ASYNC_CANCEL_APPROVED", "ASYNC_CANCEL_FAILED", "ASYNC_PAY_APPROVED", "ASYNC_PAY_FAILED"]
"""웹훅 실행 트리거

수동 웹훅 재발송, 가상계좌 입금, 비동기 취소 승인 시 발생한 웹훅일 때 필드의 값이 존재합니다.
"""

