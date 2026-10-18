from cryptography.hazmat.primitives.hpke import Suite,KEM,KDF,AEAD,MLKEM768X25519PrivateKey
#from cryptography.hazmat.primitives.asymmetric import x25519,mlkem
from cryptography.hazmat.primitives import serialization
from pathlib import Path
import getpass

s = Suite(KEM.MLKEM768_X25519,KDF.HKDF_SHA384,AEAD.CHACHA20_POLY1305)
print('HPKE/sha384/ChaCha20Poly1305 decryption')

x2privkf = input('path to the X25519 private key file(PEM format is required):')
if not x2privkf:
  x2privkf = 'X25519-private-key.pem'
with open(x2privkf,'rb') as f: #x2
  x2privk = serialization.load_pem_private_key(f.read(),getpass.getpass('password of the x25519 key:').encode())

mlprivkf = input('path to the ML-KEM768 private key file(PEM format is required):')
if not mlprivkf:
  mlprivkf = 'ML-KEM768-private-key.pem'
with open(mlprivkf,'rb') as f: #ml
  mlprivk = serialization.load_pem_private_key(f.read(),getpass.getpass('password for the mlkem key:').encode())

privk = MLKEM768X25519PrivateKey(mlprivk,x2privk)

ct = Path(input('path to the encrypted file:')).read_bytes()

pt = s.decrypt(ct,privk)

Path(input('decrypted file name:')).write_bytes(pt)

print('operation completed successfully')
