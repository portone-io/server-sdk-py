import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._currency import Currency

@dataclasses.dataclass
class RegisterStoreReceiptBodyItem:
    """하위 상점 거래 정보"""
    store_business_registration_number: str = dataclasses.field(metadata={"serde_rename": "storeBusinessRegistrationNumber"})
    """하위 상점 사업자등록번호"""
    store_name: str = dataclasses.field(metadata={"serde_rename": "storeName"})
    """하위 상점명"""
    total_amount: int = dataclasses.field(metadata={"serde_rename": "totalAmount"})
    """결제 총 금액"""
    tax_free_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "taxFreeAmount", "serde_skip_if": lambda value: value is None})
    """면세액"""
    vat_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "vatAmount", "serde_skip_if": lambda value: value is None})
    """부가세액"""
    supply_amount: Optional[int] = dataclasses.field(metadata={"serde_rename": "supplyAmount", "serde_skip_if": lambda value: value is None})
    """공급가액"""
    currency: Currency = dataclasses.field()
    """통화"""

