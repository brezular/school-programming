import string

template = string.ascii_lowercase

def get_key_index(index_text, key, key_len):
    return template.index(key[index_text % key_len])

def encrypt_decrypt(file, key, mode):
    index_text = 0
    result_text = ""
    key_len = len(key)
    
    for message_letter in file:

        upper_char = False             

        if message_letter.isupper():
            upper_char = True
            message_letter = message_letter.lower()
                
        key_index = get_key_index(index_text, key, key_len)   # get lettter key
   
        if message_letter in template:
            letter_index = template.index(message_letter)

            if mode == "encrypt":
                changed_index = (letter_index + key_index) % 26
            elif mode == "decrypt":
                changed_index = (letter_index - key_index) % 26

            changed_letter = template[changed_index]
            index_text+=1

        else:
            changed_letter = message_letter

        if upper_char:
            changed_letter = changed_letter.upper()

        result_text+= changed_letter
    return result_text
