'''
Jason Bachman
CSC 110 - Homework 7
Due 4/1/19
'''

def polyalphabetic(plaintext, codeword):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    #cipher as blank string
    ciphertext = ""
    #shift_word as empty list
    shift_word = []
    #loops through codeword to make sure there are no repeat letters
    for i in range(len(codeword)):
        if (codeword[i] not in shift_word):
            shift_word.append(codeword[i])
            #sets the new alphabet plus the codeword at the beginning
    new_alphabet = shift_word + alphabet
#loops through plaintext
    for i in range(len(plaintext)):
        #gets letter
        letter = plaintext[i]
        #gets position of that letter
        num_in_alphabet = alphabet.index(letter)
        #gets shift letter
        shift = new_alphabet[i]
        #gets shift value
        num_to_shift = alphabet.index(shift)
        #new position
        cipher_num = (num_in_alphabet + num_to_shift) % len(alphabet)
        #new letter
        cipher_letter = alphabet[cipher_num]
        #new text
        ciphertext = ciphertext + cipher_letter
    return ciphertext
a = polyalphabetic("iloveyou","heart")
print(a)