from Crypto.Protocol import HPKE
from Crypto.PublicKey import ECC
import questionary
from base64 import b64encode
import sys

print("HPKE X448+CHACHA20POLY1305")

pubn = input("公鑰名稱(PEM、X448格式，若無，則按Enter)：")
if pubn == "":
    privkey = ECC.generate(curve='curve448')
    pubkey = privkey.public_key()

    print("設定金鑰...")
    privn = input("私鑰名稱(不用加.pem)：")
    pwd = questionary.password("私鑰密碼：").ask()
    with open(privn + ".pem", "wt") as f:
        data = privkey.export_key(format='PEM',\
                                passphrase=pwd.encode("utf-8"),\
                                protection='scryptAndAES256-GCM',\
                                prot_params={'iteration_count':2097152,'salt_size': 128})
        f.write(data)

    with open(f"{input('公鑰名稱(不用加.pem)：')}.pem", "wt") as f:
        data = privkey.public_key().export_key(format='PEM')
        f.write(data)
    print("儲存成功！")
else:
    try:
        with open(pubn, "rt") as f:
            data = f.read()
            pubkey = ECC.import_key(data)
    except Exception as e:
        print(f"檔案讀取錯誤，請檢查名稱及金鑰格式是否正確。錯誤碼:{e}")
        sys.exit(1)

encryptor = HPKE.new(receiver_key=pubkey,\
                     aead_id=HPKE.AEAD.CHACHA20_POLY1305)

pt = input("要加密的文字：").encode("utf-8")
sys.stdout.write("\033[F\033[K")
print("_已隱藏密文。")
aad = input("要驗證的文字(aad，無加密，可留空)：").encode("utf-8")

ct = encryptor.seal(pt, auth_data=aad)

print(f"密文(base64)：{b64encode(ct)}")

encn = input("密文檔名(不用加).enc：")
if encn:
    with open(encn + ".enc", 'wb') as f:
        f.write(encryptor.enc)
        f.write(ct)
else:
    print("僅輸出密文，不儲存。")

print(f"臨時CHACHA20POLY1305金鑰：{b64encode(encryptor.enc)}")

print("程序結束。")
