
# - pip install cryptography

import base64
import os
from cryptography.fernet import Fernet

class CryptoTool:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def display_key(self):
        print(f"Generated Key (base64): {self.key.decode()}")

    def encrypt_message(self, message):
        if not isinstance(message, bytes):
            message = message.encode()
        encrypted = self.cipher_suite.encrypt(message)
        return encrypted.decode()

    def decrypt_message(self, token):
        try:
            decrypted = self.cipher_suite.decrypt(token.encode())
            return decrypted.decode()
        except Exception as e:
            return f"Decryption failed: {str(e)}"

    def save_key(self, filename="crypto_key.key"):
        with open(filename, "wb") as f:
            f.write(self.key)
        print(f"Key saved to {filename}")

    def load_key(self, filename="crypto_key.key"):
        if not os.path.exists(filename):
            print("Key file not found.")
            return False
        with open(filename, "rb") as f:
            self.key = f.read()
        self.cipher_suite = Fernet(self.key)
        print(f"Key loaded from {filename}")
        return True

def main():
    tool = CryptoTool()

    while True:
        print("\n=== Advanced Encrypt/Decrypt Tool ===")
        print("1. Display Key")
        print("2. Save Key to File")
        print("3. Load Key from File")
        print("4. Encrypt Message")
        print("5. Decrypt Message")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            tool.display_key()
        elif choice == '2':
            tool.save_key()
        elif choice == '3':
            tool.load_key()
        elif choice == '4':
            msg = input("Enter message to encrypt: ")
            enc = tool.encrypt_message(msg)
            print(f"Encrypted: {enc}")
        elif choice == '5':
            token = input("Enter token to decrypt: ")
            dec = tool.decrypt_message(token)
            print(f"Decrypted: {dec}")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
            
