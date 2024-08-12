from portone_server_sdk._openapi._schemas._channel_specific_failure_invalid_request import (
    ChannelSpecificFailureInvalidRequest,
)
from portone_server_sdk._openapi._schemas._channel_specific_failure_pg_provider import (
    ChannelSpecificFailurePgProvider,
)

type ChannelSpecificFailure = (
    ChannelSpecificFailureInvalidRequest | ChannelSpecificFailurePgProvider
)
"""ChannelSpecificFailure"""
