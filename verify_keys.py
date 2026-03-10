# run this once as: python verify_keys.py
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os
from dotenv import load_dotenv

load_dotenv()

private_pem = base64.b64decode(os.getenv("JWT_PRIVATE_KEY"))
public_pem  = base64.b64decode(os.getenv("JWT_PUBLIC_KEY"))

# Load private key and derive its public key
private_key = serialization.load_pem_private_key(private_pem, password=None, backend=default_backend())
derived_public = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode()

stored_public = public_pem.decode()

print("=== Derived public key ===")
print(derived_public)
print("=== Stored public key ===")
print(stored_public)
print("=== MATCH:", derived_public.strip() == stored_public.strip(), "===")