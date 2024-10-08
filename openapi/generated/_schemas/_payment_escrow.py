from typing import Union
from portone_server_sdk._openapi._schemas._before_registered_payment_escrow import BeforeRegisteredPaymentEscrow
from portone_server_sdk._openapi._schemas._cancelled_payment_escrow import CancelledPaymentEscrow
from portone_server_sdk._openapi._schemas._confirmed_payment_escrow import ConfirmedPaymentEscrow
from portone_server_sdk._openapi._schemas._delivered_payment_escrow import DeliveredPaymentEscrow
from portone_server_sdk._openapi._schemas._registered_payment_escrow import RegisteredPaymentEscrow
from portone_server_sdk._openapi._schemas._reject_confirmed_payment_escrow import RejectConfirmedPaymentEscrow
from portone_server_sdk._openapi._schemas._rejected_payment_escrow import RejectedPaymentEscrow

PaymentEscrow = Union[BeforeRegisteredPaymentEscrow, CancelledPaymentEscrow, ConfirmedPaymentEscrow, DeliveredPaymentEscrow, RegisteredPaymentEscrow, RejectedPaymentEscrow, RejectConfirmedPaymentEscrow]
"""에스크로 정보

V1 결제 건의 경우 타입이 REGISTERED 로 고정됩니다.
"""

