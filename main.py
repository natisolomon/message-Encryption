from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()


def encrypt_message(key, message):
    cipher_suite = Fernet(key)
    encrypt_message = cipher_suite.encrypt(message.encode())
    return encrypt_message

def decrypt_message(key, encrypted_message):
    cipher_suite = Fernet(key)
    decrypt_message = cipher_suite.decrypt(encrypt_message).decode()
    return decrypt_message

if __name__ == "__main__":
    key = generate_key()
    message = input("Enter a message to encrypt: ")


    print(key)
    encrypt_message = encrypt_message(key, message)
    print(f"Encrypted Message: {encrypt_message}")



