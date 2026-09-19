from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import secrets as sc
import sys

ksize = int(input("加密位元(一般機密128、高等機密192、最高機密256，輸入數字)：")) / 8

print(f"AES-GCM-SIV {int(ksize*8)}bit 加密")

header = b"header"

dt = input("密文：").encode('utf-8')

sys.stdout.write("\033[F\033[K")

print("_已隱藏密文。")

key = input("鑰匙：")

sys.stdout.write("\033[F\033[K")

print("_已隱藏鑰匙。")

if sc.compare_digest(key, ''):
    global cipher
    key = b64encode(get_random_bytes(int(ksize)))
    print(f"以下是你的鑰匙：\r\n\
            (用黑色輸出，請勿外洩)\r\n\
            \033[30m\r\n\
            {str(key).replace("b'",'').replace("'",'')}")

nonce = get_random_bytes(16)
cipher = AES.new(b64decode(key), AES.MODE_SIV,nonce = nonce)

#cipher.update(header)

ecd , tag = cipher.encrypt_and_digest(dt)

nonce = b64encode(cipher.nonce).decode('utf-8')

print("\033[0m")

ct = b64encode(ecd).decode('utf-8')

print(f"可公開內容：\r\n\
        Nonce:{nonce}\r\n\
        校驗和：{b64encode(tag).decode('utf-8')}\r\n\
        密文：{ct}")

