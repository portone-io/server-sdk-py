from ._generated import _schemas as schemas
from ._generated._sync_api import PortOneApi

__all__ = ["PortOneApi", "schemas"]

PortOneApi.__module__ = "portone_server_sdk.sync"
for schema in dir(schemas):
    if not schema.startswith("_"):
        getattr(schemas, schema).__module__ = "portone_server.sdk.sync.schemas"
