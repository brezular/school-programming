"""
Program uses the ROT13 cipher to encrypt the content of 'rot13-unencrypted.txt'
and saves the result to a new file, 'rot13-encrypted.txt'.

To check the encryption, you can use an online tool like:
https://www.dcode.fr/rot-13-cipher
"""

import string

# Generates a string of all lowercase characters from 'a' to 'z'
chars = string.ascii_lowercase

def convert_row(row):
    encrypted_row = ""

    for char in row:
        is_capital = char.isupper()
            
        if char.isalpha():                                      # Encrypt only chars
            char =  char.lower()                                # Convert char to lower
            char_index  = chars.index(char)                     # Get index of char

            # Apply the ROT13 shift. The modulo operator ensures the index
            # wraps around from 'z' back to 'a' if needed.
            char_index = (char_index + 13) % 26               

            if is_capital:
                # Get the new character and convert it to uppercase
                encrypted_row += (chars[char_index]).capitalize()  
            else:
                # Get the new character and add it to the encrypted string
                encrypted_row += chars[char_index]                
        else:
            # If the character is not a letter (e.g., a number or symbol),
            # add it to the encrypted string without changing it.
            encrypted_row += char                                     

    return encrypted_row
                
            
# +----------- Main Program ----------------------+
# Open files for reading and writing.

g = open("rot13-encrypted.txt", "w")
f = open("rot13-unencrypted.txt", "r")

for row in f:
    # Encrypt each line and write the result to the output file.
    g.write(convert_row(row))  
    
f.close()
g.close()

    






