import dataclasses

@dataclasses.dataclass
class ApplyEscrowLogisticsResponse:
    """에스크로 배송 정보 등록 성공 응답"""
    invoice_number: str = dataclasses.field(metadata={"serde_rename": "invoiceNumber"})
    """송장 번호"""
    sent_at: str = dataclasses.field(metadata={"serde_rename": "sentAt"})
    """발송 시점"""
    applied_at: str = dataclasses.field(metadata={"serde_rename": "appliedAt"})
    """에스크로 정보 등록 시점"""

