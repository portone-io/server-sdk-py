import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass(kw_only=True)
class PgProviderError:
    """PG사에서 오류를 전달한 경우"""
    type: Literal["PG_PROVIDER"]
    message: Optional[str]
    pgCode: str
    pgMessage: str

