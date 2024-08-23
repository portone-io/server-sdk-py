from typing import Union
from portone_server_sdk._openapi._schemas._cancelled_payment_cash_receipt import CancelledPaymentCashReceipt
from portone_server_sdk._openapi._schemas._issued_payment_cash_receipt import IssuedPaymentCashReceipt

PaymentCashReceipt = Union[CancelledPaymentCashReceipt, IssuedPaymentCashReceipt]
"""결제 건 내 현금영수증 정보"""

