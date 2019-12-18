import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    '''
    DOCSTRING: Check a string for pangram.
    NOTE:      Pangrams are words or sentences containing every letter of the alphabet at least once.
    EXAMPLE:   "The quick brown fox jumps over the lazy dog"
    '''
   str1 = str1.lower().replace(" ","")
    alphabet = list(alphabet)
    for letter in str1:
        if letter in alphabet:
            alphabet.remove(letter)
        else:
            pass
    return len(alphabet)== 0
