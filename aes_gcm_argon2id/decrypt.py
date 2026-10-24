import getpass
from Crypto.Cipher import AES
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
import sys
import psutil

print("AES-GCM 256 + Argon2id(Associated Data=python pycryptodome cipher-deuj2)解密")

try:
    with open(input("請輸入要解密的檔案路徑：").strip('"').strip("'"), "rb") as f:
        armem = int.from_bytes(f.read(4), byteorder='big')
        nonce = f.read(12)
        tag = f.read(16)
        salt = f.read(16)
        ct = f.read()

    mem_avail = psutil.virtual_memory().available / (1024 * 1024)  #MB
    if mem_avail / 2 <= armem: #mb
        if armem > 2048:  #VERY IMPORTANT, check if the memory cost is valid
            print(f'無效的argon2id記憶體用量:{armem}mb，請檢查檔案是否遭竄改。')
            sys.exit(1)
        print(f'可用記憶體過小，無法運行本程式，本程式須{armem}mb以上可用記憶體，請嘗試關閉其他視窗或程式然後再試一次。')
        sys.exit(1)
    else:
        print(f"已自動根據檔案調整argon2id記憶體用量，用量為{armem}mb")


    kdf = Argon2id(
        salt=salt,
        length=32,
        iterations=1,
        lanes=4,
        memory_cost= armem * 1024,  #mb
        ad=b"python pycryptodome cipher-deuj2",
        secret=None, #pepper
    )   

    key = kdf.derive(getpass.getpass("密碼：").encode())

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    pt = cipher.decrypt_and_verify(ct, tag)
except Exception as e:
    print("\033[0m")
    if str(e) == "MAC check failed":
        print("\033[5;101m 警告！訊息遭竄改！ \033[0m")
    print(f"解密錯誤。\r\n\
           錯誤碼：{e}\r\n\
           檢查是否輸入錯誤，或訊息遭竄改。")
    sys.exit(1)
else:
    with open(input("解密後檔案路徑：").strip('"').strip("'"), "wb") as f:
        f.write(pt)
    print(f"解密完成，解密後檔案路徑: {f.name}")
