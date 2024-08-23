import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._currency import Currency

@dataclasses.dataclass
class RegisterStoreReceiptBodyItem:
    """하위 상점 거래 정보"""
    storeBusinessRegistrationNumber: str
    """하위 상점 사업자등록번호"""
    storeName: str
    """하위 상점명"""
    totalAmount: int
    """결제 총 금액"""
    taxFreeAmount: Optional[int]
    """면세액"""
    vatAmount: Optional[int]
    """부가세액"""
    supplyAmount: Optional[int]
    """공급가액"""
    currency: Currency
    """통화"""

