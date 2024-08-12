from portone_server_sdk._openapi._schemas._deleted_billing_key_info import DeletedBillingKeyInfo
from portone_server_sdk._openapi._schemas._issued_billing_key_info import IssuedBillingKeyInfo

type BillingKeyInfo = DeletedBillingKeyInfo | IssuedBillingKeyInfo
"""빌링키 정보"""

