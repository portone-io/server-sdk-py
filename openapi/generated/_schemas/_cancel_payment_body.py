import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._cancel_payment_body_refund_account import CancelPaymentBodyRefundAccount
from portone_server_sdk._openapi._schemas._cancel_requester import CancelRequester

@dataclasses.dataclass
class CancelPaymentBody:
    """결제 취소 요청 입력 정보"""
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId", "serde_skip_if": lambda value: value is None})
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    amount: Optional[int] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """취소 총 금액
    
    값을 입력하지 않으면 전액 취소됩니다.
    """
    tax_free_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "taxFreeAmount", "serde_skip_if": lambda value: value is None})
    """취소 금액 중 면세 금액
    
    값을 입력하지 않으면 전액 과세 취소됩니다.
    """
    vat_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "vatAmount", "serde_skip_if": lambda value: value is None})
    """취소 금액 중 부가세액
    
    값을 입력하지 않으면 자동 계산됩니다.
    """
    reason: str = dataclasses.field()
    """취소 사유"""
    requester: Optional[CancelRequester] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """취소 요청자
    
    고객에 의한 취소일 경우 Customer, 관리자에 의한 취소일 경우 Admin으로 입력합니다.
    """
    current_cancellable_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "currentCancellableAmount", "serde_skip_if": lambda value: value is None})
    """결제 건의 취소 가능 잔액
    
    본 취소 요청 이전의 취소 가능 잔액으로써, 값을 입력하면 잔액이 일치하는 경우에만 취소가 진행됩니다. 값을 입력하지 않으면 별도의 검증 처리를 수행하지 않습니다.
    """
    refund_account: Optional[CancelPaymentBodyRefundAccount] = dataclasses.field(metadata={"serde_rename": "refundAccount", "serde_skip_if": lambda value: value is None})
    """환불 계좌
    
    계좌 환불일 경우 입력합니다. 계좌 환불이 필요한 경우는 가상계좌 환불, 휴대폰 익월 환불 등이 있습니다.
    """

