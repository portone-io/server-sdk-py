from typing import Union
from portone_server_sdk._openapi._schemas._failed_pg_billing_key_issue_response import FailedPgBillingKeyIssueResponse
from portone_server_sdk._openapi._schemas._issued_pg_billing_key_issue_response import IssuedPgBillingKeyIssueResponse

PgBillingKeyIssueResponse = Union[FailedPgBillingKeyIssueResponse, IssuedPgBillingKeyIssueResponse]
"""채널 별 빌링키 발급 응답"""

