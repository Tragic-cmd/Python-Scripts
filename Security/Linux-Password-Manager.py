import os
import json
from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self):
        self.passwords = {}
        self.key = None
        self.fernet = None
        self.load_key()

    def load_key(self):
        key_file_path = os.path.expanduser("~/.password_manager_key")

        if os.path.exists(key_file_path):
            with open(key_file_path, "rb") as key_file:
                self.key = key_file.read()
                self.fernet = Fernet(self.key)
        else:
            self.key = Fernet.generate_key()
            self.fernet = Fernet(self.key)
            with open(key_file_path, "wb") as key_file:
                key_file.write(self.key)

    def add_password(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        description = input("Enter description: ")
        encrypted_password = self.fernet.encrypt(password.encode()).decode()
        self.passwords[description] = {"username": username, "password": encrypted_password}

        with open(os.path.expanduser("~/.passwords"), "w") as password_file:
            json.dump(self.passwords, password_file)

    def get_password(self):
        description = input("Enter description: ")
        password = self.passwords.get(description)

        if not password:
            print("Password not found.")
            return

        username = password["username"]
        encrypted_password = password["password"]
        decrypted_password = self.fernet.decrypt(encrypted_password.encode()).decode()
        print(f"Username: {username}\nPassword: {decrypted_password}")

    def list_passwords(self):
        for description, password in self.passwords.items():
            print(description)

    def delete_password(self):
        description = input("Enter description: ")
        if description in self.passwords:
            del self.passwords[description]
            with open(os.path.expanduser("~/.passwords"), "w") as password_file:
                json.dump(self.passwords, password_file)
        else:
            print("Password not found.")

    def change_key(self):
        old_key = self.key
        self.load_key()
        new_key = self.key

        for description, password in self.passwords.items():
            encrypted_password = password["password"].encode()
            decrypted_password = self.fernet.decrypt(encrypted_password).decode()
            encrypted_password = self.fernet.encrypt(decrypted_password.encode()).decode()
            password["password"] = encrypted_password

        with open(os.path.expanduser("~/.passwords"), "w") as password_file:
            json.dump(self.passwords, password_file)

        os.remove(os.path.expanduser(f"~/.password_manager_key_{old_key.hex()}"))

    def backup_passwords(self):
        backup_file_path = os.path.expanduser("~/.passwords.backup")

        if os.path.exists(backup_file_path):
            print("Backup file already exists.")
            return

        with open(backup_file_path, "w") as backup_file:
            json.dump(self.passwords, backup_file)

    def restore_passwords(self):
        backup_file_path = input("Enter backup file path: ")

        if not os.path.exists(backup_file_path):
            print("Backup file not found.")
            return

        with open(backup_file_path, "r") as backup_file:
            self.passwords = json.load(backup_file)

        with open(os.path.expanduser("~/.passwords"), "w") as password_file:
            json.dump(self.passwords, password_file)

    def quit(self):
        print("Goodbye!")
        exit()
