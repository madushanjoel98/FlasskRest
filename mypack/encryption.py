import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def set_key(secret_key):
    key = hashlib.sha1(secret_key.encode('utf-8')).digest()
    key = key[:16]  # use only the first 16 bytes
    return key


def i_encrypt(text, secret_key):
    key = set_key(secret_key)
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
    return base64.b64encode(encrypted_text).decode('utf-8')


def i_decrypt(encrypted_text, secret_key):
    key = set_key(secret_key)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(base64.b64decode(encrypted_text)), AES.block_size)
    return decrypted_text.decode('utf-8')


if __name__ == "__main__":
    secret_key = "PLC@123"
    encrypted = i_encrypt("Test1", secret_key)
    print("Encrypted:", encrypted)

    decrypted = i_decrypt("As5NXKE8msdGzYTQEuOLTQ==", secret_key)
    print("Decrypted:", decrypted)
