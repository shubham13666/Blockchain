import datetime
import hashlib
import json

from Keys_Sign_Verify import Generate_Key_Value_Pair


def create_transaction(self, to, amount):  # for a transaction we only need the amount of coins and the receiver
    timestamp = datetime.datetime.utcnow().isoformat()
    signature = self.generate_signature(self.generate_signable_transaction(self.get_pubkey(), to, amount, timestamp))

    transaction = {
        "from": self.public_key,
        "to": to,
        "amount": amount,
        "signature": signature,
        "timestamp": timestamp,
        "hash": 0
    }
    transaction["hash"] = self.calculate_transaction_hash(transaction)


def generate_signable_transaction(self, from_address, to_address, amount, timestamp):  # generates a transaction which needs to be signed.

    return ":".join((from_address, to_address, amount, timestamp))


def calculate_transaction_hash(self, transaction):
    """
    Calculates sha-256 hash of transaction

    :param transaction: transaction
    :type transaction: dict(from, to, amount, timestamp, signature, (hash))

    :return: sha256 hash
    :rtype: str
    """
    # pop hash so method can calculate transactions pre or post hash
    data = transaction.copy()
    data.pop("hash", None)
    data_json = json.dumps(data, sort_keys=True)
    hash_object = hashlib.sha256(data_json)
    return hash_object.hexdigest()



