import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._bank import Bank

@dataclasses.dataclass
class CancelPaymentBodyRefundAccount:
    """고객 정보 입력 형식"""
    bank: Bank = dataclasses.field()
    """은행"""
    number: str = dataclasses.field()
    """계좌번호"""
    holder_name: str = dataclasses.field(metadata={"serde_rename": "holderName"})
    """예금주"""
    holder_phone_number: Optional[str] = dataclasses.field(metadata={"serde_rename": "holderPhoneNumber", "serde_skip_if": lambda value: value is None})
    """예금주 연락처 - 스마트로 가상계좌 결제인 경우에 필요합니다."""

