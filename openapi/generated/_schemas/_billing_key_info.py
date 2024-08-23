from typing import Union
from portone_server_sdk._openapi._schemas._deleted_billing_key_info import DeletedBillingKeyInfo
from portone_server_sdk._openapi._schemas._issued_billing_key_info import IssuedBillingKeyInfo

BillingKeyInfo = Union[DeletedBillingKeyInfo, IssuedBillingKeyInfo]
"""빌링키 정보"""

