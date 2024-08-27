import dataclasses
from typing import Any, Optional
from portone_server_sdk._openapi._schemas._identity_verification_method import IdentityVerificationMethod
from portone_server_sdk._openapi._schemas._identity_verification_operator import IdentityVerificationOperator
from portone_server_sdk._openapi._schemas._send_identity_verification_body_customer import SendIdentityVerificationBodyCustomer

@dataclasses.dataclass
class SendIdentityVerificationBody:
    """본인인증 요청을 위한 입력 정보"""
    store_id: Optional[str] = dataclasses.field(metadata={"serde_rename": "storeId", "serde_skip_if": lambda value: value is None})
    """상점 아이디
    
    접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
    """
    channel_key: str = dataclasses.field(metadata={"serde_rename": "channelKey"})
    """채널 키"""
    customer: SendIdentityVerificationBodyCustomer = dataclasses.field()
    """고객 정보"""
    custom_data: Optional[str] = dataclasses.field(metadata={"serde_rename": "customData", "serde_skip_if": lambda value: value is None})
    """사용자 지정 데이터"""
    bypass: Optional[Any] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고)"""
    operator: IdentityVerificationOperator = dataclasses.field()
    """통신사"""
    method: IdentityVerificationMethod = dataclasses.field()
    """본인인증 방식"""

