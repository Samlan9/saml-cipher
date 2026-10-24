from Crypto.Cipher import AES
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
import os
import getpass
import re
import psutil
import sys

print('\033[5;102m AES-GCM 256 \033[0m + Argon2id(Associated Data=python pycryptodome cipher-deuj2)加密')

mem_avail = psutil.virtual_memory().available / (1024 * 1024)  #MB
if mem_avail <= 1024: #1gb
    print(f'可用記憶體過小，無法運行本程式，本程式須1gb以上可用記憶體，請嘗試關閉其他視窗或程式然後再試一次。')
    sys.exit(1)
else:
    armem = round(mem_avail / 5) #mb,int
    if armem > 2048:   
        armem = 2048   #max
    elif armem < 4:
        armem = 4    #min
    print(f"已自動根據此系統調整argon2id記憶體用量，用量為{armem}mb")

nonce = os.urandom(12)
salt = os.urandom(16)
kdf = Argon2id(
    salt=salt,
    length=32,
    iterations=1,
    lanes=4,
    memory_cost= armem * 1024,  #mb
    ad=b"python pycryptodome cipher-deuj2",
    secret=None, #pepper
)


with open(input("請輸入要加密的檔案的路徑：").strip('"').strip("'"), "rb") as f:
    ptf = f.read()

while 1:
    pwd = getpass.getpass("密碼：")
    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%\-\_\+\[\]\\^&~`\'*()܍±,.?\":{}|<>]).{5,40}$", pwd):
        if input("密碼過弱，建議 5-40 字元，含大小寫字母、數字及特殊符號，按enter來更改，\033[101m 輸入weak來確定使用此弱密碼\033[0m:").lower().strip() == 'weak':
            break
    else:
        break

key = kdf.derive(pwd.encode())

cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

ct , tag = cipher.encrypt_and_digest(ptf)

with open(input("密文檔案路徑:").strip('"').strip("'"),'wb') as f:
    f.write(armem.to_bytes(4, byteorder='big') + nonce + tag + salt + ct)

print(f"加密完成，密文檔案路徑: {f.name}")
