import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._bank import Bank

@dataclasses.dataclass
class CancelPaymentBodyRefundAccount:
    """고객 정보 입력 형식"""
    bank: Bank
    """은행"""
    number: str
    """계좌번호"""
    holderName: str
    """예금주"""
    holderPhoneNumber: Optional[str]
    """예금주 연락처 - 스마트로 가상계좌 결제인 경우에 필요합니다."""

