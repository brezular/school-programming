"""
A command-line tool for Vigenere cipher encryption and decryption.
test: https://cryptii.com/pipes/vigenere-cipher
"""

import sys
import string
import vigenere

# Files
key_file = "key.txt"       # file with encryption key
plain_file = "text.txt"    # file with the text to encrypt
enc_file = "text-enc.txt"  # encrypted file


def show_menu():
    print(f"The program uses Vigenere cipher encrypt/decrypt text using the key in the file '{key_file}'")
    print(f"\n1. Encrypt text in the file '{plain_file}' and save it to '{enc_file}'")
    print(f"2. Decrypt text in the file '{enc_file}' and save it to '{plain_file}'")
    print(f"q. Quit program\n")

def check_file(file, subject):
    try:
        with open(file, "r") as f:
            text = f.read().strip() # remove white chars from the beggining and end of entire text 
            if not text:
                print(f"ERROR! {subject} not found in file {file}, exiting")
                sys.exit(1)
            return text
        
    except FileNotFoundError:
        print(f"ERROR! File '{file}' not found, exiting")
        sys.exit(1)

# Read user choice
def read_choice():
    while True:
        choice = input("Enter your choice: ")
        if choice not in "12q":
            print(f"Wrong choice!")
        else:
            return choice

def save_content(file, result_text):
    with open(file, "w") as g:
        g.write(result_text)

def check_key(key):
    for char in key:
        if not char.islower():
            return False
    return True

# ------------------------ MAIN --------------------------+

show_menu()
choice = read_choice()

# Read enc/dec key from file
key = check_file(key_file, "key")

# Key must contain lower letters only
if not check_key(key):
    print(f"ERROR! Key must contain lower letters only, exiting")
    sys.exit(1)
          
if choice == "1":
    plain_text = check_file(plain_file, "plain text")
    print(f"\nINFO: File '{plain_file}' for encryption and file '{key_file}' found")

    result_text = vigenere.encrypt_decrypt(plain_text, key, mode="encrypt")
    save_content(enc_file, result_text)

    print(f"\n*** SUCCESS: File '{enc_file}' with encrypted content has been created ***")
    sys.exit(0)

elif choice == "2":
    encrypted_text = check_file(enc_file, "encrypted text")
    print(f"\nINFO: File '{enc_file}' for decription and file '{key_file}' found")

    result_text = vigenere.encrypt_decrypt(encrypted_text, key, mode="decrypt")
    save_content(plain_file, result_text)

    print(f"\n*** SUCCESS: File '{plain_file}' with decrypted content has been created ***")
    sys.exit(0)

elif choice == "q":
    sys.exit(0)






        
    













    

