from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import base64


class Crypto:
    @staticmethod
    def generate_key_pair() -> tuple[str, str]:
        """Generates an RSA key pair and returns (private_key, public_key) in PEM format."""
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()

        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        ).decode()

        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ).decode()
        return private_pem, public_pem

    @staticmethod
    def get_public_key_from_private(private_key_pem: str) -> str:
        """Extracts and returns the public key from a given private key (PEM format)."""
        private_key = serialization.load_pem_private_key(
            private_key_pem.encode(), password=None
        )
        public_key = private_key.public_key()

        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ).decode()

    @staticmethod
    def get_signature(message: str, private_key_pem: str) -> str:
        """Signs a message using the provided private key."""
        private_key = serialization.load_pem_private_key(
            private_key_pem.encode(), password=None
        )

        signature = private_key.sign(
            message.encode(), padding.PKCS1v15(), hashes.SHA256()
        )

        return base64.b64encode(signature).decode()

    @staticmethod
    def verify_signature(message: str, public_key_pem: str, signature: str) -> bool:
        """Verifies the signature using the provided public key."""
        public_key = serialization.load_pem_public_key(public_key_pem.encode())
        signature_bytes = base64.b64decode(signature)

        try:
            public_key.verify(
                signature_bytes, message.encode(), padding.PKCS1v15(), hashes.SHA256()
            )
            return True
        except:
            return False
