import dataclasses
from portone_server_sdk._openapi._schemas._page_info import PageInfo
from portone_server_sdk._openapi._schemas._payment_schedule import PaymentSchedule


@dataclasses.dataclass(kw_only=True)
class GetPaymentSchedulesResponse:
    """결제 예약 다건 조회 성공 응답 정보"""

    items: list[PaymentSchedule]
    """조회된 결제 예약 건 리스트"""
    page: PageInfo
    """조회된 페이지 정보"""
