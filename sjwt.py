#by t.me/awsi5
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
            print(f"Failed to install {library_name}.")
            sys.exit(1)

def print_loading_bar(iteration, total, bar_length=40):
    filled_length = int(bar_length * iteration // total)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f'\r[{bar}] Attempt {iteration}/{total}')
    sys.stdout.flush()

def brute_force_jwt_secret(token, wordlist_path):
    if not os.path.exists(wordlist_path):
        print(f"Wordlist file '{wordlist_path}' not found. Make sure the file exists.")
        return

    with open(wordlist_path, 'r', encoding='utf-8') as file:
        wordlist = [line.strip() for line in file]

    def try_key(secret_key):
        try:
            decode(token, secret_key, algorithms=["HS256"])
            return f"Success! The secret key is: {secret_key}"
        except (InvalidTokenError, DecodeError):
            return None

    total_words = len(wordlist)
    
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(try_key, key) for key in wordlist]
        for count, future in enumerate(futures, 1):
            result = future.result()
            print_loading_bar(count, total_words)
            if result:
                print(f"\n\n{result}")
                return
        print("\nBrute force failed. No valid key found.")

if __name__ == "__main__":
    try:
        from jwt import decode, InvalidTokenError, DecodeError
    except ImportError:
        install_missing_library('PyJWT')
        sys.exit(1)

    encoded_jwt = input("Enter your JWT:").strip()
    if not encoded_jwt:
        print('Error: JWT input is required and cannot be left empty.')
    else:
        print('wait..\n')
        wordlist_path = 'wordlist.txt'
        brute_force_jwt_secret(encoded_jwt, wordlist_path)
