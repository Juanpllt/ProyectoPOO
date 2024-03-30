from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

private_key = rsa.generate_private_key(
     public_exponent=65537,
     key_size=2048,
     backend=default_backend()
)

public_key = private_key.public_key()

print(public_key)

print(private_key)

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

message = b"A message I want to sign"
signature = private_key.sign(
     message,
     padding.PSS(
         mgf=padding.MGF1(hashes.SHA256()),
         salt_length=padding.PSS.MAX_LENGTH
     ),
     hashes.SHA256()
)

message = b"Dato para cifrar"
ciphertext = public_key.encrypt(
     message,
     padding.OAEP(
         mgf=padding.MGF1(algorithm=hashes.SHA256()),
         algorithm=hashes.SHA256(),
         label=None
     )
 )

plaintext = private_key.decrypt(
     ciphertext,
     padding.OAEP(
         mgf=padding.MGF1(algorithm=hashes.SHA256()),
         algorithm=hashes.SHA256(),
         label=None
     )
 )
print(plaintext)
print(message)