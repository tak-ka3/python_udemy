import string
import random

from Crypto.Cipher import AES

print(AES.block_size)
print(string.ascii_letters)
key = ''.join(
  random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
# 初期ベクトル
iv = ''.join(
  random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
print(key)
print('*****************')

plaintext = 'lgjalhfoghoajfbhakhg'
cipher = AES.new(key, AES.MODE_CBC, iv) # ここで暗号化の方法を設定
padding_length = AES.block_size - len(plaintext) % AES.block_size
plaintext += chr(padding_length) * padding_length # padding_lengthという整数をchrで文字にしている
# print('KKKKKKKKK',plaintext, 'KKKK')
cipher_text = cipher.encrypt(plaintext)
print(cipher_text)

print('******************')

cipher2 = AES.new(key, AES.MODE_CBC, iv)
decrypted_text = cipher2.decrypt(cipher_text)
print(decrypted_text)
print(decrypted_text[-1])
print(decrypted_text[:-decrypted_text[-1]])