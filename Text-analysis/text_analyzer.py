import string
import url

page = "https://www.gutenberg.org/files/1342/1342-h/1342-h.htm"


#  generate template with lowercase characters
template =  string.ascii_lowercase 

# find the total number of letters in the file
def get_count_chars(content):
    char_count= 0
    for char in content:         
        if str.isalpha(char):   
            char_count+=1        
    return char_count         # total number of letters

#---------------- Main Program ----------------#
content = url.read_text(page).lower() # convert all chars to lowercase

char_count = get_count_chars(content)

for char in template:
    # count occurrences of char (both lower and upper case)
    occurence = content.count(char)
    
    if occurence > 0:                      # ak je znak v subore, vypiseme jeho statistiku                         
                   
        print(f"Letter '{char}'(including'{char.capitalize()}'): occurence count: {occurence}/{char_count}, \
{round(occurence/char_count*100, 2)}%")
