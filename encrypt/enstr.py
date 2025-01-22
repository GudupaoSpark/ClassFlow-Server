import uuid
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os


def encrypt_bytes(data: bytes, pw:str) -> str:
    pw = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    """加密二进制数据（返回Hex字符串）"""
    key = bytes.fromhex(pw)[:32]
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = iv + cipher.encrypt(pad(data, AES.block_size))
    return encrypted.hex()

def decrypt_bytes(encrypted_hex: str, pw: str) -> bytes:
    pw = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    """解密Hex字符串为二进制数据"""
    encrypted = bytes.fromhex(encrypted_hex)
    iv = encrypted[:16]
    ciphertext = encrypted[16:]
    key = bytes.fromhex(pw)[:32]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size)

def encrypt_text(text: str, pw: str) -> str:
    """加密文本（返回Hex字符串）"""
    encrypted = encrypt_bytes(text.encode('utf-8'), pw)
    return encrypted

def decrypt_text(encrypted_hex: str, pw: str) -> str:
    """解密Hex字符串为文本"""
    data = decrypt_bytes(encrypted_hex, pw)
    return data.decode('utf-8')

if __name__ == "__main__":
    pw = "123456"
    text = "Hello, world!"
    byte = b"Hello, world!"
    encrypted = encrypt_text(text, pw)
    print(encrypted)
    decrypted = decrypt_text(encrypted, pw)
    print(decrypted)
    encrypted = encrypt_bytes(byte, pw)
    print(encrypted)
    decrypted = decrypt_bytes(encrypted, pw)
    print(decrypted)