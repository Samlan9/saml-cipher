from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
import sys

print("DES CTR")

print("\033[101m WARNING: DES is VERY WEAK and should not be used for sensitive data. \033[0m")
print("正在產生DES金鑰...")

nm = input("DES金鑰名稱(須加副檔名)：")

try:
    with open(nm, "rb") as f:
        key = f.read()
except Exception as e:
    print(f"讀取錯誤{e}")
    sys.exit(1)

ctr = Counter.new(64)
cipher = DES.new(key, DES.MODE_CTR, counter=ctr)

nm = input("DES密文名稱(不須加副檔名.enc)：")

try:
    with open(nm + ".enc", "rb") as f:
        #ctr = f.read(64)
        ct = f.read()
except Exception as e:
    print(f"讀取錯誤{e}")
    sys.exit(1)

ct = cipher.decrypt(ct)

print(f"明文：{ct.decode()}")
