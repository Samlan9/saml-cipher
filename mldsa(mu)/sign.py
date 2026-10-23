from cryptography.hazmat.primitives.asymmetric import mldsa
from cryptography.hazmat.primitives import serialization
import getpass
import sys

"""
External Mu
參數集	NIST 安全等級	等效傳統安全性	公鑰大小 (Public Key)	私鑰大小 (Private Key)*	簽章大小 (Signature)
ML-DSA-44	Category 2	約等同 AES-128 / SHA-256	1,312 bytes	2,560 bytes	2,420 bytes
ML-DSA-65	Category 3	約等同 AES-192	1,952 bytes	4,032 bytes	3,309 bytes
ML-DSA-87	Category 5	約等同 AES-256	2,592 bytes	4,896 bytes	4,627 bytes
"""

if sys.version_info[:2] < (3,11):
    print("You're running an incompatible version of python. Only version >=3.11 is acceptable.")

print("MLDSA65(MU) SIGN")


privkfp = input('enter the path to MLDSA65 private key:')
try:
  with open(privkfp,'rb') as f:
    privk = serialization.load_pem_private_key(f.read(), password=getpass.getpass('private Key password:').encode())
except FileNotFoundError:
    print(f"{privkfp} - file not found.")
    sys.exit(1)
if not privkfp:
  print('generating the keys...')
  privk = mldsa.MLDSA65PrivateKey.generate()
  pubk = privk.public_key()

  pwd = getpass.getpass('private Key password:').encode()
  privkf = privk.private_bytes(
      encoding=serialization.Encoding.PEM,
      format=serialization.PrivateFormat.PKCS8,
      encryption_algorithm=serialization.BestAvailableEncryption(pwd)
  )
  privkfn = 'MLDSA65-private-key.pem'
  with open(privkfn,'wb') as f:
    f.write(privkf)
  print(f'private key saved as {privkfn}')
  del(privkf)
  with open('MLDSA65-public-key.pem','wb') as f:
    f.write(pubk.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))
    print('public key saved as MLDSA65-public-key.pem')

inputf = input('enter the path to the file to sign:')
with open(inputf,'rb') as f:
    data = f.read()

hasher = mldsa.MLDSAMuHasher(public_key=privk.public_key())

hasher.update(data)

mu = hasher.finalize()

with open(inputf+'.sig','wb') as f:
    f.write(privk.sign_mu(mu))
    print(f'signature saved as {inputf}.sig')

