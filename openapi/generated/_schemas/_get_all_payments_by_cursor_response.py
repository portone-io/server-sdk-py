import dataclasses
from portone_server_sdk._openapi._schemas._payment_with_cursor import PaymentWithCursor

@dataclasses.dataclass
class GetAllPaymentsByCursorResponse:
    """결제 건 커서 기반 대용량 다건 조회 성공 응답 정보"""
    items: list[PaymentWithCursor]
    """조회된 결제 건 및 커서 정보 리스트"""

