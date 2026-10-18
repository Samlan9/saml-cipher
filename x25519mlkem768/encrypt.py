from cryptography.hazmat.primitives.hpke import KDF,Suite,KEM,AEAD,MLKEM768X25519PrivateKey,MLKEM768X25519PublicKey
from cryptography.hazmat.primitives.asymmetric import x25519,mlkem
from cryptography.hazmat.primitives import serialization
from pathlib import Path

s = Suite(KEM.MLKEM768_X25519,KDF.HKDF_SHA384,AEAD.CHACHA20_POLY1305) #initialization

print('Post-Quantum HPKE,with ChaCha20_Poly1305 for better mobile performance and SHA384 for anti Collision')

x2pubfn = input("File path to x25519 public key(PEM format is required, press Enter directly if you don't have the key):")
mlpubfn = input("file path to mlkem768 public key(PEM format is required, press Enter directly if you don't have the key):")
if x2pubfn and mlpubfn:
  with open(x2pubfn,'rb') as f: #x2
    x2pub = serialization.load_pem_public_key(f.read())
  with open(mlpubfn,'rb') as f: #ml
    mlpub = serialization.load_pem_public_key(f.read())

else:
  print('generating the keys... this may take a few moment.')
#private key
  x2priv = x25519.X25519PrivateKey.generate()
  mlpriv = mlkem.MLKEM768PrivateKey.generate()

#public key
  x2pub = x2priv.public_key()
  mlpub = mlpriv.public_key()

  print('---')

  for n,ca in (('X25519',x2priv),('ML-KEM768',mlpriv)):
    pw = input(f'{n} private Key password:').encode()
    privkf = ca.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(pw)
    )
    fn = f'{n}-private-key.pem'

    Path(fn).write_bytes(privkf)
    print(f'saved {n} private key as {fn}')

  for n,ca in (('X25519',x2pub),('ML-KEM768',mlpub)):
    pubkf = ca.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    fn = f'{n}-public-key.pem'

    Path(fn).write_bytes(pubkf)
    print(f'saved {n} public key as {fn}')

keypub = MLKEM768X25519PublicKey(mlpub,x2pub)

pt = input('text to encrypt(press enter directly if you want to encrypt a file/folder):').encode()

if not pt:
  p = input('path to the file/folder: ')
  if Path(p).absolute().is_dir():
    import shutil
    shutil.make_archive(p,'zip',p)
    p = f'{p}.zip'

  with open(p,'rb') as f:
    pt = f.read()

ct = s.encrypt(pt,keypub)

fn = input('output file name:')
with open(fn,'wb') as f:
  f.write(ct)

print('operation completed successfully!')
