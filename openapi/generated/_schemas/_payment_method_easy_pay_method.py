from typing import Union
from portone_server_sdk._openapi._schemas._payment_method_card import PaymentMethodCard
from portone_server_sdk._openapi._schemas._payment_method_easy_pay_method_charge import PaymentMethodEasyPayMethodCharge
from portone_server_sdk._openapi._schemas._payment_method_transfer import PaymentMethodTransfer

PaymentMethodEasyPayMethod = Union[PaymentMethodCard, PaymentMethodEasyPayMethodCharge, PaymentMethodTransfer]
"""간편 결제 수단"""

