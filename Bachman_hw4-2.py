'''
Jason Bachman
CSC 110 - Homework 4 - Working with Python Functions
Due 2/25/19
'''

#the function
def subString(word,length):
    #makes the list
    result = []
    #for loop that slices the word into the desired segments
    for i in range(len(word)-1):
        cut = slice(i,i+length)
        if length == len(word[cut]):
            result.append(word[cut])
#prints results
    print(result)
    
        
