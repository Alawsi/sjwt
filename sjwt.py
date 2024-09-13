import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

def install_missing_library(library_name):
    print(f'You need to install "{library_name}".')
    print(f'You can copy this command "pip install {library_name}"')

    action = input(f'\n\nDo you want to install the {library_name} library (y/n)? : ').strip().lower()

    if action == "y":
        print(f"Attempting to install {library_name}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])
            print(f"{library_name} installed successfully. Running the tool now...\n")
        except subprocess.CalledProcessError:
            print(f"Failed to install {library_name}. Please install it manually by running 'pip install {library_name}'.")
            sys.exit(1)
    else:
        print("Please install the required library and rerun the program.")
        sys.exit(1)

try:
    import jwt
    from jwt.exceptions import InvalidTokenError, DecodeError
except ModuleNotFoundError:
    install_missing_library('PyJWT')
    import jwt
    from jwt.exceptions import InvalidTokenError, DecodeError

def brute_force_jwt_secret(token, wordlist_path):
    if not os.path.exists(wordlist_path):
        print(f"Wordlist file '{wordlist_path}' not found. Make sure the file exists.")
        return

    with open(wordlist_path, 'r', encoding='utf-8') as file:
        wordlist = [line.strip() for line in file]

    def try_key(secret_key):
        try:
            jwt.decode(token, secret_key, algorithms=["HS256"])
            return f"Success! The secret key is: {secret_key}"
        except (InvalidTokenError, DecodeError):
            return None

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(try_key, wordlist))

    for count, result in enumerate(results, 1):
        if result:
            print(f"\n\n{count} - {result}")
            return
        else:
            print(f"{count} - Failed attempt with key: {wordlist[count-1]}")

    print("Brute force failed. No valid key found.")

if __name__ == "__main__":
    encoded_jwt = input("Enter your JWT: ").strip()
    if not encoded_jwt:
        print('Error: JWT input is required and cannot be left empty.')
    else:
        wordlist_path = 'wordlist.txt'
        brute_force_jwt_secret(encoded_jwt, wordlist_path)
