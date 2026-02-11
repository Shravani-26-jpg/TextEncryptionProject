from aes_module import *
from rsa_module import *

# Generate keys
aes_key = generate_key()
private_key, public_key = generate_keys()

while True:
    print("\n=== ADVANCED TEXT ENCRYPTION TOOL ===")
    print("1. AES Encrypt Message")
    print("2. RSA Encrypt Message")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        msg = input("Enter message: ")
        encrypted = encrypt_text(msg, aes_key)
        print("AES Encrypted:", encrypted)

        decrypted = decrypt_text(encrypted, aes_key)
        print("AES Decrypted:", decrypted)

    elif choice == "2":
        msg = input("Enter message: ")
        encrypted = encrypt_message(msg, public_key)
        print("RSA Encrypted:", encrypted)

        decrypted = decrypt_message(encrypted, private_key)
        print("RSA Decrypted:", decrypted)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")

