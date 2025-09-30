import random
import string

template = string.ascii_lowercase

# generate 26 random letters
def key():
    key = ""
    while len(key) != 26: 
        char = random.choice(template)
        if char not in key:
            key += char
    return key
