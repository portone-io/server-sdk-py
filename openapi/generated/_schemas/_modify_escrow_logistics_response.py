import dataclasses

@dataclasses.dataclass
class ModifyEscrowLogisticsResponse:
    """에스크로 배송 정보 수정 성공 응답"""
    invoice_number: str = dataclasses.field(metadata={"serde_rename": "invoiceNumber"})
    """송장 번호"""
    sent_at: str = dataclasses.field(metadata={"serde_rename": "sentAt"})
    """발송 시점"""
    modified_at: str = dataclasses.field(metadata={"serde_rename": "modifiedAt"})
    """에스크로 정보 수정 시점"""

