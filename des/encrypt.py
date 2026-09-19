from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
import sys
from base64 import b64encode as b64e

print("DES CTR")

print("\033[101m WARNING: DES is VERY WEAK and should not be used for sensitive data. \033[0m")
print("正在產生DES金鑰...")

nm = input("DES金鑰名稱(須加副檔名)：")

try:
    with open(nm, "rb") as f:
        key = f.read()
except FileNotFoundError:
    key = get_random_bytes(8)

    try:
        with open(nm, "wb") as f:
            f.write(key)
            print(f"已產生DES金鑰，並寫入{nm}")
    except Exception as e:
        print(f"寫入錯誤{e}")

ctr = Counter.new(64)
cipher = DES.new(key, DES.MODE_CTR, counter=ctr)

pt = input("要加密的文字：").encode("utf-8")
sys.stdout.write("\033[F\033[K")
print("_已隱藏密文。")

ct = cipher.encrypt(pt)
ct_nm = input("密文檔名(不須加副檔名.enc)：")
try:
    with open(f"{ct_nm}.enc", "wb") as f:
        #f.write(ctr)
        f.write(ct)
except Exception as e:
    print(f"寫入錯誤{e}")
    sys.exit(1)

print(f"密文(base64)：{b64e(ct)}")