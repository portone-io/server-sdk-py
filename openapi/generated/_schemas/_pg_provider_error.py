import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class PgProviderError:
    """PG사에서 오류를 전달한 경우"""
    type: Literal["PG_PROVIDER"] = dataclasses.field()
    message: Optional[str] = dataclasses.field(metadata={"serde_skip_if": lambda value: value is None})
    pg_code: str = dataclasses.field(metadata={"serde_rename": "pgCode"})
    pg_message: str = dataclasses.field(metadata={"serde_rename": "pgMessage"})

