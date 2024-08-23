import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._payment_escrow_receiver_input import PaymentEscrowReceiverInput
from portone_server_sdk._openapi._schemas._payment_escrow_sender_input import PaymentEscrowSenderInput
from portone_server_sdk._openapi._schemas._payment_logistics import PaymentLogistics
from portone_server_sdk._openapi._schemas._payment_product import PaymentProduct

@dataclasses.dataclass
class ModifyEscrowLogisticsBody:
    """에스크로 배송 정보 수정 입력 정보"""
    storeId: Optional[str]
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    sender: Optional[PaymentEscrowSenderInput]
    """에스크로 발송자 정보"""
    receiver: Optional[PaymentEscrowReceiverInput]
    """에스크로 수취인 정보"""
    logistics: PaymentLogistics
    """에스크로 물류 정보"""
    sendEmail: Optional[bool]
    """이메일 알림 전송 여부
    
    에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
    """
    products: Optional[list[PaymentProduct]]
    """상품 정보"""

