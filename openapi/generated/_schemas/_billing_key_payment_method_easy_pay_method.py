from portone_server_sdk._openapi._schemas._billing_key_payment_method_card import (
    BillingKeyPaymentMethodCard,
)
from portone_server_sdk._openapi._schemas._billing_key_payment_method_easy_pay_charge import (
    BillingKeyPaymentMethodEasyPayCharge,
)
from portone_server_sdk._openapi._schemas._billing_key_payment_method_transfer import (
    BillingKeyPaymentMethodTransfer,
)

type BillingKeyPaymentMethodEasyPayMethod = (
    BillingKeyPaymentMethodCard
    | BillingKeyPaymentMethodEasyPayCharge
    | BillingKeyPaymentMethodTransfer
)
"""간편 결제 수단"""
