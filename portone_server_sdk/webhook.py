import codecs
import hmac
import time
from collections.abc import Mapping
from typing import Union

from portone_server_sdk._errors import InvalidInputError, WebhookVerificationError

_required_headers = {
    "webhook-id": str,
    "webhook-timestamp": str,
    "webhook-signature": str,
}


def verify(
    secret: Union[str, bytes, bytearray], payload: str, headers: Mapping[str, str]
) -> None:
    """웹훅 페이로드를 검증합니다.

    Args:
        secret (str | bytes | bytearray): 웹훅 시크릿
        payload (str): 웹훅 페이로드
        headers (Mapping[str, str]): 웹훅 요청 시 포함된 헤더

    Raises:
        InvalidInputError: 입력받은 시크릿이 유효하지 않을 때 발생합니다.
        WebhookVerificationError: 웹훅 검증에 실패했을 때 발생합니다.
    """
    for header_name in _required_headers:
        header_value = headers.get(header_name)
        if not isinstance(header_value, _required_headers[header_name]):
            raise WebhookVerificationError("MISSING_REQUIRED_HEADERS")

    msg_timestamp = headers["webhook-timestamp"]
    verify_timestamp(msg_timestamp)

    msg_id = headers["webhook-id"]
    expected_signature = sign(secret, msg_id, msg_timestamp, payload)

    msg_signature = headers["webhook-signature"]
    for versioned_signagure in msg_signature.split(" "):
        split = versioned_signagure.split(",", 3)
        if len(split) < 2:
            continue
        version, signature, *_ = split
        if version != "v1":
            continue
        try:
            signature_decoded = codecs.decode(signature.encode(), "base64")
        except ValueError:
            continue

        if hmac.compare_digest(signature_decoded, expected_signature):
            return
    raise WebhookVerificationError("NO_MATCHING_SIGNATURE")


WEBHOOK_TOLERANCE_IN_SECONDS = 5 * 60  # 5분


def verify_timestamp(timestamp_header: str) -> None:
    now = int(time.time())
    try:
        timestamp = int(timestamp_header)
    except ValueError:
        raise WebhookVerificationError("INVALID_SIGNATURE")
    if now - timestamp > WEBHOOK_TOLERANCE_IN_SECONDS:
        raise WebhookVerificationError("TIMESTAMP_TOO_OLD")
    if timestamp > now + WEBHOOK_TOLERANCE_IN_SECONDS:
        raise WebhookVerificationError("TIMESTAMP_TOO_NEW")


def sign(
    secret: Union[str, bytes, bytearray], msg_id: str, msg_timestamp: str, payload: str
) -> bytes:
    raw_secret = get_raw_secret(secret)
    to_sign = f"{msg_id}.{msg_timestamp}.{payload}"
    return hmac.digest(raw_secret, to_sign.encode(), "sha256")


_prefix = "whsec_"


def get_raw_secret(secret: Union[str, bytes, bytearray]) -> Union[bytes, bytearray]:
    if isinstance(secret, (bytes, bytearray)):
        raw_secret = secret
    elif isinstance(secret, str):
        secret_base64 = secret[len(_prefix) :] if secret.startswith(_prefix) else secret
        try:
            raw_secret = codecs.decode(secret_base64.encode(), "base64")
        except ValueError:
            raise InvalidInputError(
                "`secret` 파라미터가 올바른 Base64 문자열이 아닙니다."
            )
    else:
        raise InvalidInputError("`secret` 파라미터의 타입이 잘못되었습니다.")

    if len(raw_secret) == 0:
        raise InvalidInputError("시크릿은 비어 있을 수 없습니다.")

    return raw_secret
