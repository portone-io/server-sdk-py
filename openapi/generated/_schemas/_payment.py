from typing import Union
from portone_server_sdk._openapi._schemas._cancelled_payment import CancelledPayment
from portone_server_sdk._openapi._schemas._failed_payment import FailedPayment
from portone_server_sdk._openapi._schemas._paid_payment import PaidPayment
from portone_server_sdk._openapi._schemas._partial_cancelled_payment import PartialCancelledPayment
from portone_server_sdk._openapi._schemas._pay_pending_payment import PayPendingPayment
from portone_server_sdk._openapi._schemas._ready_payment import ReadyPayment
from portone_server_sdk._openapi._schemas._virtual_account_issued_payment import VirtualAccountIssuedPayment

Payment = Union[CancelledPayment, FailedPayment, PaidPayment, PartialCancelledPayment, PayPendingPayment, ReadyPayment, VirtualAccountIssuedPayment]
"""결제 건"""

