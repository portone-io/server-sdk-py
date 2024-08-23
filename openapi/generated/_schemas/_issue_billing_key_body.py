import dataclasses
from typing import Any, Optional
from portone_server_sdk._openapi._schemas._customer_input import CustomerInput
from portone_server_sdk._openapi._schemas._instant_billing_key_payment_method_input import InstantBillingKeyPaymentMethodInput

@dataclasses.dataclass
class IssueBillingKeyBody:
    """빌링키 발급 요청 양식"""
    storeId: Optional[str]
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    method: InstantBillingKeyPaymentMethodInput
    """빌링키 결제 수단 정보"""
    channelKey: Optional[str]
    """채널 키
    
    채널 키 또는 채널 그룹 ID 필수
    """
    channelGroupId: Optional[str]
    """채널 그룹 ID
    
    채널 키 또는 채널 그룹 ID 필수
    """
    customer: Optional[CustomerInput]
    """고객 정보"""
    customData: Optional[str]
    """사용자 지정 데이터"""
    bypass: Optional[Any]
    """PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)"""
    noticeUrls: Optional[list[str]]
    """웹훅 주소
    
    빌링키 발급 시 요청을 받을 웹훅 주소입니다.
    상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
    입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
    """

