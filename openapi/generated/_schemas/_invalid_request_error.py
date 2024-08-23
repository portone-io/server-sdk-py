import dataclasses
from typing import Literal, Optional

@dataclasses.dataclass
class InvalidRequestError:
    """요청된 입력 정보가 유효하지 않은 경우
    
    허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
    """
    type: Literal["INVALID_REQUEST"]
    message: Optional[str]

