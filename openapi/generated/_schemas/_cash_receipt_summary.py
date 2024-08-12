import dataclasses


@dataclasses.dataclass(kw_only=True)
class CashReceiptSummary:
    """현금영수증 내역"""

    issueNumber: str
    """발행 번호"""
    url: str
    """현금 영수증 URL"""
    pgReceiptId: str
    """PG사 현금영수증 아이디"""
