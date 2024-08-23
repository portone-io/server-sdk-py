import dataclasses
from typing import Any, Optional
from portone_server_sdk._openapi._schemas._identity_verification_method import IdentityVerificationMethod
from portone_server_sdk._openapi._schemas._identity_verification_operator import IdentityVerificationOperator
from portone_server_sdk._openapi._schemas._send_identity_verification_body_customer import SendIdentityVerificationBodyCustomer

@dataclasses.dataclass
class SendIdentityVerificationBody:
    """본인인증 요청을 위한 입력 정보"""
    storeId: Optional[str]
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    channelKey: str
    """채널 키"""
    customer: SendIdentityVerificationBodyCustomer
    """고객 정보"""
    customData: Optional[str]
    """사용자 지정 데이터"""
    bypass: Optional[Any]
    """PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)"""
    operator: IdentityVerificationOperator
    """통신사"""
    method: IdentityVerificationMethod
    """본인인증 방식"""

