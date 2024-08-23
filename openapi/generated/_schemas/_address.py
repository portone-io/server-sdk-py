from typing import Union
from portone_server_sdk._openapi._schemas._one_line_address import OneLineAddress
from portone_server_sdk._openapi._schemas._separated_address import SeparatedAddress

Address = Union[OneLineAddress, SeparatedAddress]
"""분리 형식 주소

oneLine(한 줄 형식 주소) 필드는 항상 존재합니다.
"""

