from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_text(text, key):
    cipher = Fernet(key)
    return cipher.encrypt(text.encode())

def decrypt_text(ciphertext, key):
    cipher = Fernet(key)
    return cipher.decrypt(ciphertext).decode()
