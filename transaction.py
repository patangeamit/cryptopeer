from dataclasses import dataclass, asdict, field
from crypto import Crypto
import hashlib
import json


@dataclass
class Transaction:
    sender_public_key: str
    receiver_public_key: str
    amount: int
    signature: str
    hash_value: str = field(init=False, repr=False)
    input: str = field(default_factory=list)
    output: str = field(default_factory=list)
    transaction_fee: int = field(default=0)

    def __post_init__(self):
        data_dict = {k: v for k, v in self.__dict__.items() if k != "hash_value"}
        self.hash_value = self.compute_hash(data_dict)

    def compute_hash(self, dict) -> str:
        """Generate SHA-256 hash of the serialized dataclass data."""
        data_string = json.dumps(dict, sort_keys=True)
        return hashlib.sha256(data_string.encode()).hexdigest()
