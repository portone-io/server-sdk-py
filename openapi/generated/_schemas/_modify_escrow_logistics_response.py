import dataclasses

@dataclasses.dataclass
class ModifyEscrowLogisticsResponse:
    """에스크로 배송 정보 수정 성공 응답"""
    invoiceNumber: str
    """송장 번호"""
    sentAt: str
    """발송 시점"""
    modifiedAt: str
    """에스크로 정보 수정 시점"""

