# import our own module - file generate_key.py
import generate_key

import string 

# Files
key_file = "key.txt"       # file with encryption key
plain_file = "text.txt"    # file with the text to encrypt
enc_file = "text-enc.txt"  # encrypted file

# postupnost od a po z
template =  string.ascii_lowercase

# Vypis menu
def show_menu():
    print(f"The program will encrypt/decrypt text using the key in the file '{key_file}'")
    print(f"\n1. Generate key and save it to '{key_file}'")
    print(f"2. Encrypt text in the file '{plain_file}' and save it to '{enc_file}'")
    print(f"3. Decrypt text in the file '{enc_file}' and save it to '{plain_file}'")
    print(f"q. Quit program\n")

# check if file exists
def check_file(file, action):
    try:
        with open(file, action) as f:
            return True
    except FileNotFoundError:
        return False

# Read user choice
def read_choice():
    while True:
        choice = input("Enter your choice: ")
        if choice not in "123q":
            print(f"Wrong choice!")
        else:
            return choice

# Generate key and save to file
def save_key(key_file):
    # use the function kluc() from module generate_key.py
    key = generate_key.key()
    with open(key_file, "w") as f:
        f.write(key)

# Read key from file 
def read_key(key_file):
    with open(key_file) as f:
        return f.readline()

# Encyption or decryption 
def change_text(file1, key_file, file2, str1, str2):
    result_text = ""
    
    with open(file1, "r") as f:
        original_text = f.read()        # read original_text file 

    # Iterate through the file to either encrypt or decrypt
    for letter in original_text:
        capital_letter = False      # reset for each char
        
        if letter in str1:   # if char is either in template or in key file
            # convert capital to lower letter and remember it
            if letter.isupper():
                letter = letter.lower()
                capital_letter = True
                
            char_position = str1.index(letter)  # we get position of char either in template of key file

            # Lookup character in key or template at the same postion           
            changed_letter = str2[char_position]

            # Convert lower to capital if letter was capital
            if capital_letter:
               changed_letter = changed_letter.upper() 

            # Add encrypted or decrypted char do result text
            result_text += changed_letter   
        else:
            result_text += letter   # add unchanged character to result text

    # add encrypted or decrypted text to the either plain text or encrypted text
    with open(file2, "w") as g:
        g.write(result_text)              
          
        
# +-------- MAIN ------------+

show_menu()

# read user's choice
choice = read_choice()

if choice == "1":
    # If key file exists, do not generate it
    
    if check_file(key_file, "r"):
        print(f"\nERROR! Key file '{key_file}' already exists, key was not generated")

    # key file does not exist, so we generate it
    else:
        save_key(key_file)

        # Check if the key was saved to disk
        if check_file(key_file, "r"):
            print(f"\n*** SUCCESS: File '{key_file}' with key was generated, exiting ***")
        else:
            print(f"\nERROR! File '{key_file}' with key was NOT generated, exiting")

elif choice == "2":
    # If plain text file or key file does not exist, do not generate enc file
    if check_file(plain_file, "r") and check_file(key_file, "r"):
        print(f"\nINFO: File '{plain_file}' for encryption and file '{key_file}' found")

        change_text(plain_file, key_file, enc_file, template, read_key(key_file))

        print(f"\n*** SUCCESS: File '{enc_file}' with encrypted content has been created ***")
    else:
        print(f"\nERROR! File '{plain_file}' for encryption, or '{key_file}' with key not found, exiting")

elif choice == "3":
    # if enc file or key file does not exist, do not generate plain file
    if check_file(enc_file, "r") and check_file(key_file, "r"):
        print(f"\nINFO: File '{enc_file}' for decryption and file '{key_file}' found")
        
        change_text(enc_file, key_file, plain_file, read_key(key_file), template)

        print(f"\n*** SUCCESS: File '{plain_file}' with decrypted content has been created ***")
    else:
        print(f"\n ERROR! File '{enc_file}' for decryption, or '{key_file}' with key not found, exiting")
        



        
    






