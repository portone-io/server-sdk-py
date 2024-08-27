import dataclasses
from typing import Literal, Optional
from portone_server_sdk._openapi._schemas._identity_verification_verified_customer import IdentityVerificationVerifiedCustomer
from portone_server_sdk._openapi._schemas._selected_channel import SelectedChannel

@dataclasses.dataclass
class VerifiedIdentityVerification:
    """완료된 본인인증 내역"""
    status: Literal["VERIFIED"] = dataclasses.field()
    """본인인증 상태"""
    id: str = dataclasses.field()
    """본인인증 내역 아이디"""
    channel: Optional[SelectedChannel] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    """사용된 본인인증 채널"""
    verified_customer: IdentityVerificationVerifiedCustomer = dataclasses.field(metadata={"serde_rename": "verifiedCustomer"})
    """인증된 고객 정보"""
    custom_data: Optional[str] = dataclasses.field(metadata={"serde_rename": "customData", "serde_skip_if": lambda value: value is None})
    """사용자 지정 데이터"""
    requested_at: str = dataclasses.field(metadata={"serde_rename": "requestedAt"})
    """본인인증 요청 시점"""
    updated_at: str = dataclasses.field(metadata={"serde_rename": "updatedAt"})
    """업데이트 시점"""
    status_changed_at: str = dataclasses.field(metadata={"serde_rename": "statusChangedAt"})
    """상태 업데이트 시점"""
    verified_at: str = dataclasses.field(metadata={"serde_rename": "verifiedAt"})
    """본인인증 완료 시점"""
    pg_tx_id: str = dataclasses.field(metadata={"serde_rename": "pgTxId"})
    """본인인증 내역 PG사 아이디"""
    pg_raw_response: str = dataclasses.field(metadata={"serde_rename": "pgRawResponse"})
    """PG사 응답 데이터"""

