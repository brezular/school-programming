import msoffcrypto
import sys
import io
import time
import datetime

from msoffcrypto.exceptions import InvalidKeyError, DecryptionError

"""
Exit:
0     - pass found
1     - file not found
99    - pass not found
"""

office_file = "crackme.docx"
decrypted_file = f"dec-{office_file}"
password_file = "passwords.txt"

def convert_seconds(start_time):
    n = int(time.time() - start_time)
    return str(datetime.timedelta(seconds = n))


# -------------- MAIN --------------------------------------"

# io.BytesIO() acts as a file in RAM where the decrypted content will be stored.
decrypted = io.BytesIO()

start_time = time.time()

try:
    # 1. Load the entire content of the encrypted Office file into RAM once
    office_content = io.BytesIO()
    with open(office_file, "rb") as g:
        office_content.write(g.read())  

    # 2. Initialize the decryption object using the content in RAM
    encrypted_text = msoffcrypto.OfficeFile(office_content)
        
    # 3. Start dictionary attack
    with open(password_file, "r") as f:
        print(f"\nDictionary attack against: '{office_file}' started")
        print(f"Passwords are loaded from: '{password_file}'")
        
        for heslo in f:
            heslo = heslo.strip()        

            try:
                # Attempt to load the key
                encrypted_text.load_key(password=heslo)

                # Move cursor to the beginning (0) and remove all previous data
                decrypted.seek(0)
                decrypted.truncate(0)
                
                # If key is loaded, attempt decryption
                encrypted_text.decrypt(decrypted)              # decrypt to RAM
                print(f"\n*** SUCCESS! Password: {heslo} found and stored to: '{decrypted_file}' ***")
                           
                # Reset stream cursor again before reading for final file write
                decrypted.seek(0)

                # Write decrypted content from RAM to a new file
                with open(decrypted_file, "wb") as h:
                    h.write(decrypted.read())

                elapsed_time = convert_seconds(start_time)
                print(f"Elapsed time: {elapsed_time}")   

                sys.exit(0)

            except InvalidKeyError:    # bad password
                continue
                    
            except DecryptionError:    # password has bad format, e.g. is blank
                continue

except FileNotFoundError:
    print(f"\nERROR! Either file '{password_file}' or '{office_file}' are missing, exiting")
    sys.exit(2)


# --- If loop finishes without finding a password ---
print(f"\n*** INFO! Password not found, exiting ***")

elapsed_time = convert_seconds(start_time)
print(f"Elapsed time: {elapsed_time}")

sys.exit(99)



   
