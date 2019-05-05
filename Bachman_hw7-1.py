'''
Jason Bachman
CSC 110 - Homework 7
Due 4/1/19
'''


def caesar_plus(plaintext, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    # initialize ciphertext as blank string
    ciphertext = ""
    # loop through the length of the plaintext
    for i in range(len(plaintext)):
        # get the i'th letter from the plaintext
        letter = plaintext[i]
        # find the number position of the ith letter
        num_in_alphabet = alphabet.index(letter)
        # find the number position of the cipher by adding the shift
        cipher_num = (num_in_alphabet + shift + i) % len(alphabet)
        # find the cipher letter for the cipher number you computed
        cipher_letter = alphabet[cipher_num]
        # add the cipher letter to the ciphertext
        ciphertext = ciphertext + cipher_letter
        # return the computed ciphertext
    return ciphertext

def uncaesar_plus(ciphertext, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    plaintext = ""
    # loop through the length of the ciphertext
    for i in range(len(ciphertext)):
        # get the i'th letter
        letter = ciphertext[i]
        # find the number position of the ith letter
        num_in_alphabet = alphabet.index(letter)
        # find the number position of the plain by subtracting the shift
        plain_num = (num_in_alphabet - shift - i) % len(alphabet)
        #find the letter
        plain_letter = alphabet[plain_num]
        #build the word
        plaintext = plaintext + plain_letter
    return plaintext

a=caesar_plus("heyemily",2)
print(a)

b=uncaesar_plus(a,2)
print(b)