import os
import getpass
import bcrypt
import json
from cryptography.fernet import Fernet

PASSWORDS_FILE = 'secret.json'
KEY_FILE = '.key'

def get_master_key():
    """Get or create the master key from user input and store securely"""
    if os.path.exists(KEY_FILE):
        # Load existing key from file
        with open(KEY_FILE, 'rb') as f:
            master_key = f.read()
    else:
        # Prompt user to create a new key
        while True:
            password = getpass.getpass(prompt='Create a master key (minimum 8 characters): ')
            if len(password) < 8:
                print('Master key must be at least 8 characters long.')
            else:
                password_confirm = getpass.getpass(prompt='Confirm master key: ')
                if password == password_confirm:
                    # Hash the password using bcrypt and store securely
                    master_key = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                    with open(KEY_FILE, 'wb') as f:
                        f.write(master_key)
                    break
                else:
                    print('Passwords do not match. Please try again.')
    return master_key

def encrypt_data(data, key):
    """Encrypt data using Fernet symmetric encryption"""
    if not isinstance(data, bytes):
        data = data.encode()
    if not isinstance(key, bytes):
        key = key.encode()
    hashed_key = bcrypt.hashpw(key, bcrypt.gensalt())
    decoded_key = bcrypt.checkpw(key, hashed_key)
    f = Fernet(decoded_key)
    encrypted_data = f.encrypt(data)
    return encrypted_data

def decrypt_data(data, key):
    """Decrypt data using Fernet symmetric encryption"""
    if not isinstance(data, bytes):
        data = data.encode()
    if not isinstance(key, bytes):
        key = key.encode()
    hashed_key = bcrypt.hashpw(key, bcrypt.gensalt())
    decoded_key = bcrypt.checkpw(key, hashed_key)
    f = Fernet(decoded_key)
    decrypted_data = f.decrypt(data)
    return decrypted_data.decode()

def add_password():
    """Prompt user for a new password and add it to the password store"""
    service = input('Enter the name of the service: ')
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')
    
    # Load existing passwords
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, 'r') as f:
            passwords = json.load(f)
    else:
        passwords = {}
    
    # Encrypt password with master key and add to passwords
    master_key = get_master_key()
    encrypted_password = encrypt_data(password, master_key)
    passwords[service] = {'username': username, 'password': encrypted_password.decode()}
    
    # Save updated passwords
    with open(PASSWORDS_FILE, 'w') as f:
        json.dump(passwords, f)
    
    print('Password added successfully.')

def list_passwords():
    """Print a list of all services and usernames in the password store"""
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, 'r') as f:
            passwords = json.load(f)
            for service, data in passwords.items():
                print(f'{service}: {data["username"]}')
    else:
        print('No passwords stored yet.')

def get_password():
    """Retrieve and print a password for a given service"""
    service = input('Enter the name of the service: ')
    with open(PASSWORDS_FILE, 'r') as f:
        passwords = json.load(f)
    if service in passwords:
        encrypted_password = passwords[service]
        decrypted_password = decrypt_data(encrypted_password, MASTER_KEY)
        print(f'Password for {service}: {decrypted_password.decode()}')
    else:
        print(f'No password saved for {service}.')

def add_password():
    """Add a new password for a service"""
    service = input('Enter the name of the service: ')
    password = getpass.getpass(prompt='Enter the password: ')
    encrypted_password = encrypt_data(password, MASTER_KEY)
    with open(PASSWORDS_FILE, 'r+') as f:
        passwords = json.load(f)
        passwords[service] = encrypted_password.decode()
        f.seek(0)
        json.dump(passwords, f, indent=4)
        f.truncate()

def main():
    """Main function to manage password manager"""
    # Get or create the master key
    master_key = get_master_key()

    # Load existing passwords from file
    passwords = load_passwords(PASSWORDS_FILE, master_key)
    
    while True:
        print('Select an option:')
        print('1. Get a password')
        print('2. Add a password')
        print('3. Quit')
        choice = input('Enter your choice: ')
        if choice == '1':
            get_password()
        elif choice == '2':
            add_password()
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
