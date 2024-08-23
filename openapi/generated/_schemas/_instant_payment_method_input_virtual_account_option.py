import dataclasses
from typing import Optional
from portone_server_sdk._openapi._schemas._instant_payment_method_input_virtual_account_option_fixed import InstantPaymentMethodInputVirtualAccountOptionFixed
from portone_server_sdk._openapi._schemas._instant_payment_method_input_virtual_account_option_type import InstantPaymentMethodInputVirtualAccountOptionType

@dataclasses.dataclass
class InstantPaymentMethodInputVirtualAccountOption:
    """가상계좌 발급 방식"""
    type: InstantPaymentMethodInputVirtualAccountOptionType
    """발급 유형"""
    fixed: Optional[InstantPaymentMethodInputVirtualAccountOptionFixed]
    """고정식 가상계좌 발급 방식
    
    발급 유형을 FIXED 로 선택했을 시에만 입력합니다.
    """

