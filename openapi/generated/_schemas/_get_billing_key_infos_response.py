import dataclasses
import serde
from portone_server_sdk._openapi._schemas._billing_key_info import BillingKeyInfo
from portone_server_sdk._openapi._schemas._page_info import PageInfo

@serde.serde(tagging=serde.Untagged)
@dataclasses.dataclass
class GetBillingKeyInfosResponse:
    """빌링키 다건 조회 성공 응답 정보"""
    items: list[BillingKeyInfo]
    """조회된 빌링키 리스트"""
    page: PageInfo
    """조회된 페이지 정보"""

