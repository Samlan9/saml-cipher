from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import questionary
#from base64 import b64decode
#from dialog import Dialog
import sys

print("RSA 4096 + PKCS#1 OAEP")

privn = input("私鑰名稱(要加.pem)：")
with open(privn, "rt") as f:
    data = f.read()
    pwd = questionary.password("私鑰密碼：").ask()
    try:
        privkey = RSA.import_key(data,pwd.encode("utf-8"))
    except Exception as e:
        print(f"讀取私鑰時發生錯誤，請檢查格式及密碼是否正確。錯誤碼：{e}")
        sys.exit(1)

ctn = input("密文檔案(要加.enc):")
with open(ctn,"rb") as f:
    ct = f.read()

#enc = b64decode(input("臨時公鑰：").replace("b'",'').replace("'",''))
decryptor = PKCS1_OAEP.new(privkey)

try:
    pt = decryptor.decrypt(ct)
except ValueError:
    print("解密失敗，請檢查私鑰及密文是否正確。")
    sys.exit(1)

print(f"明文：{pt}")
