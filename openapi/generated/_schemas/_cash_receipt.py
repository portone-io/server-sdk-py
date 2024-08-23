from typing import Union
from portone_server_sdk._openapi._schemas._cancelled_cash_receipt import CancelledCashReceipt
from portone_server_sdk._openapi._schemas._issue_failed_cash_receipt import IssueFailedCashReceipt
from portone_server_sdk._openapi._schemas._issued_cash_receipt import IssuedCashReceipt

CashReceipt = Union[CancelledCashReceipt, IssuedCashReceipt, IssueFailedCashReceipt]
"""현금영수증 내역"""

