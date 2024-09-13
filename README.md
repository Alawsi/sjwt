# Sjwt (secret key JWT) | jwt-cracker | brute-force JWT
**1 - brute-force attack on a JWT (JSON Web Token) to discover its secret key**

**2 - The tool enables you to guess more than 100,000 secret keys in about 5 seconds.**


## Overview

**Sjwt** is a Python script designed to perform a brute-force attack on a JWT (JSON Web Token) to discover its secret key. It uses a provided wordlist of potential keys and attempts to decode the JWT with each key until it finds a match or exhausts the wordlist.

## Screenshot :
![Screenshot](https://github.com/Alawsi/sjwt/blob/main/Screenshot%202024-09-13%20234016.png?raw=true)


## Requirements

- Python 3.x
- `PyJWT` library (Automatically installed if missing)

 
## Usage

1. **Prepare Your Wordlist:**
   - When you download the tool, a file `wordlist.txt` will be downloaded, which contains more than 100,00 secret keys.
   - You can change the file as you like and add more, but keep the file name `wordlist.txt`
  

    
2. **Run the Script:**

   On **Windows**:
   - Download the `sjwt.py` file from the repository.
   - Open Command Prompt and navigate to the directory where `sjwt.py` is located.
   - Run the script by typing:
     ```bash
     python sjwt.py
     ```
   - Follow the prompts:
     - Type `y` to install the required library (`PyJWT`) if it's not already installed.
     - Enter your JWT token when prompted.

   On **Other Operating Systems** (Linux/MacOS):
   - Clone the repository:
     ```bash
     git clone https://github.com/Alawsi/sjwt.git
     cd sjwt
     python sjwt.py
     
   - Follow the prompts as described above.

