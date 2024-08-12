from portone_server_sdk._openapi._schemas._billing_key_payment_method_card import (
    BillingKeyPaymentMethodCard,
)
from portone_server_sdk._openapi._schemas._billing_key_payment_method_easy_pay import (
    BillingKeyPaymentMethodEasyPay,
)
from portone_server_sdk._openapi._schemas._billing_key_payment_method_mobile import (
    BillingKeyPaymentMethodMobile,
)
from portone_server_sdk._openapi._schemas._billing_key_payment_method_paypal import (
    BillingKeyPaymentMethodPaypal,
)
from portone_server_sdk._openapi._schemas._billing_key_payment_method_transfer import (
    BillingKeyPaymentMethodTransfer,
)

type BillingKeyPaymentMethod = (
    BillingKeyPaymentMethodCard
    | BillingKeyPaymentMethodEasyPay
    | BillingKeyPaymentMethodMobile
    | BillingKeyPaymentMethodPaypal
    | BillingKeyPaymentMethodTransfer
)
"""빌링키 발급 수단 정보"""
