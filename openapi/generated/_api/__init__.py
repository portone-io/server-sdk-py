from dataclasses import dataclass
from ._get_identity_verification import GetIdentityVerification
from ._send_identity_verification import SendIdentityVerification
from ._confirm_identity_verification import ConfirmIdentityVerification
from ._resend_identity_verification import ResendIdentityVerification
from ._pre_register_payment import PreRegisterPayment
from ._get_billing_key_info import GetBillingKeyInfo
from ._delete_billing_key import DeleteBillingKey
from ._get_billing_key_infos import GetBillingKeyInfos
from ._issue_billing_key import IssueBillingKey
from ._get_cash_receipt_by_payment_id import GetCashReceiptByPaymentId
from ._get_payment import GetPayment
from ._get_payments import GetPayments
from ._get_all_payments_by_cursor import GetAllPaymentsByCursor
from ._get_payment_schedule import GetPaymentSchedule
from ._get_payment_schedules import GetPaymentSchedules
from ._revoke_payment_schedules import RevokePaymentSchedules
from ._create_payment_schedule import CreatePaymentSchedule
from ._cancel_payment import CancelPayment
from ._pay_with_billing_key import PayWithBillingKey
from ._pay_instantly import PayInstantly
from ._issue_cash_receipt import IssueCashReceipt
from ._cancel_cash_receipt_by_payment_id import CancelCashReceiptByPaymentId
from ._close_virtual_account import CloseVirtualAccount
from ._apply_escrow_logistics import ApplyEscrowLogistics
from ._modify_escrow_logistics import ModifyEscrowLogistics
from ._confirm_escrow import ConfirmEscrow
from ._resend_webhook import ResendWebhook
from ._get_kakaopay_payment_order import GetKakaopayPaymentOrder
from ._register_store_receipt import RegisterStoreReceipt

@dataclass
class PortOneApi(
    GetIdentityVerification,
    SendIdentityVerification,
    ConfirmIdentityVerification,
    ResendIdentityVerification,
    PreRegisterPayment,
    GetBillingKeyInfo,
    DeleteBillingKey,
    GetBillingKeyInfos,
    IssueBillingKey,
    GetCashReceiptByPaymentId,
    GetPayment,
    GetPayments,
    GetAllPaymentsByCursor,
    GetPaymentSchedule,
    GetPaymentSchedules,
    RevokePaymentSchedules,
    CreatePaymentSchedule,
    CancelPayment,
    PayWithBillingKey,
    PayInstantly,
    IssueCashReceipt,
    CancelCashReceiptByPaymentId,
    CloseVirtualAccount,
    ApplyEscrowLogistics,
    ModifyEscrowLogistics,
    ConfirmEscrow,
    ResendWebhook,
    GetKakaopayPaymentOrder,
    RegisterStoreReceipt,
):
    pass
