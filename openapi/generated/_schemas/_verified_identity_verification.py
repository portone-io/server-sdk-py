import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._identity_verification_verified_customer import IdentityVerificationVerifiedCustomer
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@dataclasses.dataclass
class VerifiedIdentityVerification:
    """완료된 본인인증 내역"""
    status: Literal["VERIFIED"]
    """본인인증 상태"""
    id: str
    """본인인증 내역 아이디"""
    channel: Optional[SelectedChannel]
    """사용된 본인인증 채널"""
    verifiedCustomer: IdentityVerificationVerifiedCustomer
    """인증된 고객 정보"""
    customData: Optional[str]
    """사용자 지정 데이터"""
    requestedAt: str
    """본인인증 요청 시점"""
    updatedAt: str
    """업데이트 시점"""
    statusChangedAt: str
    """상태 업데이트 시점"""
    verifiedAt: str
    """본인인증 완료 시점"""
    pgTxId: str
    """본인인증 내역 PG사 아이디"""
    pgRawResponse: str
    """PG사 응답 데이터"""

