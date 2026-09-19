from Crypto.Protocol import HPKE
from Crypto.PublicKey import ECC
import questionary
from base64 import b64decode
#from dialog import Dialog
import sys

print("HPKE X448+CHACHA20POLY1305")

privn = input("私鑰名稱(不用加.pem)：")
with open(privn + ".pem", "rt") as f:
    data = f.read()
    pwd = questionary.password("私鑰密碼：").ask()
    try:
        privkey = ECC.import_key(data,pwd.encode("utf-8"))
    except Exception as e:
        print(f"讀取私鑰時發生錯誤，請檢查格式及密碼是否正確。錯誤碼：{e}")
        sys.exit(1)

ctn = input("密文檔案(不用加.enc):")
with open(ctn + ".enc","rb") as f:
    enc = f.read(56)
    ct = f.read()

#enc = b64decode(input("臨時公鑰：").replace("b'",'').replace("'",''))
decryptor = HPKE.new(receiver_key=privkey,\
                     aead_id=HPKE.AEAD.CHACHA20_POLY1305,\
                     enc = enc)

aad = input("aad(若無，可省略):").encode()

try:
    pt = decryptor.unseal(ct, auth_data=aad)
except ValueError:
#    d = Dialog(dialog="dialog")
#    d.set_background_title("decrypt.py")
#    d.msgbox("警告：訊息遭竄改。")
    print("\033[41;37m 警告：訊息遭竄改 \033[0m")
    pt = "\\不適用\\"

print(f"明文：{pt}")
