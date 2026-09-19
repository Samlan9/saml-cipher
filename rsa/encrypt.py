from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import questionary
from base64 import b64encode
import sys

print("RSA 4096 + PKCS8 + PKCS#1 OAEP + scrypt + AES256-GCM")

pubn = input("公鑰名稱(PEM格式 不用加.pem，若無，則按Enter)：")
if pubn == "":
    print("設定金鑰...")
    privkey = RSA.generate(4096)
    pubkey = privkey.public_key()

    privn = input("私鑰名稱(不用加.pem)：")
    pwd = questionary.password("私鑰密碼：").ask() 
    with open(privn + ".pem", "wb") as f:
        data = privkey.export_key(format='PEM',\
                                pkcs=8,\
                                passphrase=pwd.encode("utf-8"),\
                                protection='scryptAndAES256-GCM',\
                                prot_params={'iteration_count':2097152,'salt_size': 128})
                                #passphrase：密碼   
        f.write(data)

    with open(f"{input('公鑰名稱(不用加.pem)：')}.pem", "wb") as f:
        data = pubkey.export_key(format='PEM')
        f.write(data)
    print("儲存成功！")
else:
    try:
        with open(pubn + ".pem", "rt") as f:
            data = f.read()
            pubkey = RSA.import_key(data)
    except Exception as e:
        print(f"檔案讀取錯誤，請檢查名稱及金鑰格式是否正確。錯誤碼:{e}")
        sys.exit(1)

cipher = PKCS1_OAEP.new(pubkey)

pt = input("要加密的文字：").encode("utf-8")
sys.stdout.write("\033[F\033[K")
print("_已隱藏密文。")

ct = cipher.encrypt(pt)

print(f"密文(base64)：{b64encode(ct)}")

while 1:
    encn = input("密文檔名(不用加.enc)：")
    try:
        with open(encn + ".enc", 'wb') as f:
            f.write(ct)
        break
    except Exception as e:
        print(f"檔案寫入錯誤。錯誤碼:{e}")

print("程序結束。")
