import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._register_store_receipt_body_item import RegisterStoreReceiptBodyItem

@dataclasses.dataclass
class RegisterStoreReceiptBody:
    """영수증 내 하위 상점 거래 등록 정보"""
    items: list[RegisterStoreReceiptBodyItem] = dataclasses.field()
    """하위 상점 거래 목록"""
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId", "serde_skip_if": lambda value: value is None})
    """상점 아이디"""

