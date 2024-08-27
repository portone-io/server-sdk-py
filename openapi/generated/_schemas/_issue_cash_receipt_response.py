import dataclasses
from portone_server_sdk._openapi._schemas._cash_receipt_summary import CashReceiptSummary

@dataclasses.dataclass
class IssueCashReceiptResponse:
    """현금 영수증 발급 성공 응답"""
    cash_receipt: CashReceiptSummary = dataclasses.field(metadata={"serde_rename": "cashReceipt"})

