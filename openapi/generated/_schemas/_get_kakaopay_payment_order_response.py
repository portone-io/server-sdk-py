import dataclasses

@dataclasses.dataclass
class GetKakaopayPaymentOrderResponse:
    """카카오페이 주문 조회 응답"""
    status_code: int = dataclasses.field(metadata={"serde_rename": "statusCode"})
    """HTTP 상태 코드"""
    body: str = dataclasses.field()
    """HTTP 응답 본문 (JSON)"""

