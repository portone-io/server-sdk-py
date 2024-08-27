import dataclasses

@dataclasses.dataclass
class CashReceiptSummary:
    """현금영수증 내역"""
    issue_number: str = dataclasses.field(metadata={"serde_rename": "issueNumber"})
    """발행 번호"""
    url: str = dataclasses.field()
    """현금 영수증 URL"""
    pg_receipt_id: str = dataclasses.field(metadata={"serde_rename": "pgReceiptId"})
    """PG사 현금영수증 아이디"""

