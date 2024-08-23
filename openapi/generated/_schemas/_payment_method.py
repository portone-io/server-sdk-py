from typing import Union
from portone_server_sdk._openapi._schemas._payment_method_card import PaymentMethodCard
from portone_server_sdk._openapi._schemas._payment_method_easy_pay import PaymentMethodEasyPay
from portone_server_sdk._openapi._schemas._payment_method_gift_certificate import PaymentMethodGiftCertificate
from portone_server_sdk._openapi._schemas._payment_method_mobile import PaymentMethodMobile
from portone_server_sdk._openapi._schemas._payment_method_transfer import PaymentMethodTransfer
from portone_server_sdk._openapi._schemas._payment_method_virtual_account import PaymentMethodVirtualAccount

PaymentMethod = Union[PaymentMethodCard, PaymentMethodEasyPay, PaymentMethodGiftCertificate, PaymentMethodMobile, PaymentMethodTransfer, PaymentMethodVirtualAccount]
"""결제수단 정보"""

