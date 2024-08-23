import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._register_store_receipt_body_item import RegisterStoreReceiptBodyItem

@dataclasses.dataclass
class RegisterStoreReceiptBody:
    """영수증 내 하위 상점 거래 등록 정보"""
    items: list[RegisterStoreReceiptBodyItem]
    """하위 상점 거래 목록"""
    storeId: Optional[str]
    """상점 아이디"""

