'''
Jason Bachman
CSC 110 - Homework 4 - Working with Python Functions
Due 2/25/19
'''

#substring function from part 2
def subString(word,length):
    result = []
    for i in range(len(word)):
        cut = slice(i,i+length)
        if length == len(word[cut]):
            print(word[cut])
    
#all substring function gets all combos from a word
def allSubStrings(word):
    length = 1
    #iterates subString will all possible lengths within a word
    while length <= len(word):
        subString(word,length)
        length += 1
            

    
        
