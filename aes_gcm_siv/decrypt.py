from base64 import b64decode
from Crypto.Cipher import AES
import sys

print("AES-GCM-SIV解密")

try:
    nonce = b64decode(input("nonce:").strip())
    ecd = b64decode(input("密文：").strip())
    tag = b64decode(input("校驗和：").strip())
    key = b64decode(input("密鑰：\033[30m")).strip()
    sys.stdout.write("\033[F\033[K")
    sys.stdout.write("\033[F\033[K")
    print("_已隱藏鑰匙。")

    print("\033[0m")


    cipher = AES.new(key, AES.MODE_SIV, nonce=nonce)
    pt = cipher.decrypt_and_verify(ecd, tag)
except Exception as e:
    print("\033[0m")
    if "MAC check failed" in e:
        print("\033[5;101m 警告！訊息遭竄改！ \033[0m")
    print(f"解密錯誤。\r\n\
           錯誤碼：{e}\r\n\
           檢查是否輸入錯誤，或訊息遭竄改。")
    pt = ""

pt = pt

print(str(pt))
