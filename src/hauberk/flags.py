
from enum import Enum


class ImapFlags(Enum):
    SEEN = b'\\Seen'


class FetchFlags(Enum):
    ENVELOPE = b'ENVELOPE'
    BODY = b'RFC822'
