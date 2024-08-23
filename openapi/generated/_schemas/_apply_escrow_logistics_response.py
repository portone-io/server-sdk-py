import dataclasses

@dataclasses.dataclass
class ApplyEscrowLogisticsResponse:
    """에스크로 배송 정보 등록 성공 응답"""
    invoiceNumber: str
    """송장 번호"""
    sentAt: str
    """발송 시점"""
    appliedAt: str
    """에스크로 정보 등록 시점"""

