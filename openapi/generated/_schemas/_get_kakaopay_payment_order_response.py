import dataclasses

@dataclasses.dataclass
class GetKakaopayPaymentOrderResponse:
    """카카오페이 주문 조회 응답"""
    statusCode: int
    """HTTP 상태 코드"""
    body: str
    """HTTP 응답 본문 (JSON)"""

