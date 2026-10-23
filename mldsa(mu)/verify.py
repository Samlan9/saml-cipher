from cryptography.hazmat.primitives.asymmetric import mldsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography import exceptions
import sys

"""
參數集	NIST 安全等級	等效傳統安全性	公鑰大小 (Public Key)	私鑰大小 (Private Key)*	簽章大小 (Signature)
ML-DSA-44	Category 2	約等同 AES-128 / SHA-256	1,312 bytes	2,560 bytes	2,420 bytes
ML-DSA-65	Category 3	約等同 AES-192	1,952 bytes	4,032 bytes	3,309 bytes
ML-DSA-87	Category 5	約等同 AES-256	2,592 bytes	4,896 bytes	4,627 bytes
"""

if sys.version_info[:2] < (3,11):
    print("You're running an incompatible version of python. Only version >=3.11 is acceptable.")

print("MLDSA65(MU) VERIFY")


pubkfp = input('enter the path to MLDSA65 public key(PEM):')
try:
  with open(pubkfp,'rb') as f:
    pubk = serialization.load_pem_public_key(f.read())
except FileNotFoundError:
    print(f"{pubkfp} - file not found.")
if not pubkfp:
  print("File Not Found")
  sys.exit(1)

inputf = input('enter the path to the file to verify:')
with open(inputf,'rb') as f:
    data = f.read()

try:
    with open(f'{inputf}.sig','rb') as f:
        signature = f.read()
except FileNotFoundError:
    with open(input('.sig file name:'),'rb') as f:
        signature = f.read()

hasher = mldsa.MLDSAMuHasher(pubk)
hasher.update(data)

mu = hasher.finalize()

h = hashes.Hash(hashes.SHA384())
h.update(signature)

try:
    pubk.verify_mu(signature, mu)
except exceptions.InvalidSignature:
   print(f".sig sha384:{h.finalize().hex()} - \033[41;37m WARNING! SIGNATURE INVAILD. \033[0m")
else:
   print(f".sig sha384 {h.finalize().hex()} - signature vaild!")
