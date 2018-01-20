from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec


def generate_key_pair():
    private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())  # ec.SECP256K1 is an ecc instance.
    public_key = private_key.public_key()  # public key.


def generate_signature(message):  # generate a signature for a transaction using private key.

    return generate_key_pair().private_key.sign(message, ec.ECDSA(hashes.SHA256()))


def verification(signature, message, public_key):  # to verify the transaction

    return public_key.verify(signature, message,
                             ec.ECDSA(hashes.SHA256()))  # raises an InvalidSignatureException if signature not verified
