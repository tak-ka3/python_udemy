import string
import random

from Crypto.Cipher import AES

key = ''.join(
  random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
# 初期ベクトル
iv = ''.join(
  random.choice(string.ascii_letters) for _ in range(AES.block_size)
)

with open('plaintext', 'r') as f, open ('enc.dat', 'wb') as e:
  plaintext = f.read()
  cipher = AES.new(key, AES.MODE_CBC, iv) # ここで暗号化の方法を設定
  padding_length = AES.block_size - len(plaintext) % AES.block_size
  plaintext += chr(padding_length) * padding_length # padding_lengthという整数をchrで文字にしている
  cipher_text = cipher.encrypt(plaintext)
  e.write(cipher_text)

print('*************')

with open('plaintext', 'rb') as f, open('plaintext', 'r') as e:
  print(f.read())
  print(e.read())

print('**************')

with open('exampletext', 'wb') as f:
  f.write(b'ABCER')

with open('enc.dat', 'rb') as f:
  cipher2 = AES.new(key, AES.MODE_CBC, iv)
  decrypted_text = cipher2.decrypt(f.read())
  print(decrypted_text[:-decrypted_text[-1]])
  print(decrypted_text[:-decrypted_text[-1]].decode('utf-8'))