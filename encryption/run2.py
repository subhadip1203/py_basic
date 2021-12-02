from os import urandom
from Crypto.Cipher import AES
import base64
from hashlib import sha256

# For Generating cipher text
prive_key = "hasvcdjghsvcgjcvgwdvcw"
password = "abcd"


secret_key = sha256(password.encode("utf-8")).digest()
iv = urandom(16)
print(secret_key)
print(iv)
obj = AES.new(secret_key, AES.MODE_CBC, iv)

# Encrypt the message
message = 'Lorem Ipsum text'
print('Original message is: ', message)
encrypted_text = obj.encrypt(message)
print('The encrypted text', encrypted_text)

# Decrypt the message
rev_obj = AES.new(secret_key, AES.MODE_CBC, iv)
decrypted_text = rev_obj.decrypt(encrypted_text)
print('The decrypted text', decrypted_text.decode('utf-8'))