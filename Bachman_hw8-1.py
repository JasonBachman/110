'''
Jason Bachman
CSC 110 - Homework 7
Due 4/7/19
'''


def fletcher32(string):
    #innitializes lists and variables
    aList = []
    bList = [0]
    checksum = 0
    #starts loop
    for i in range(len(string)):
        #gets each ord value from the letters of the string
        ordvalue = ord(string[i])
        #adds it to list a
        aList.append(ordvalue)
        #gets the value for bList
        b_ord = ordvalue + bList[i]
        b_ord = b_ord % 65535
        #adds it to b list
        bList.append(b_ord)
        #adds together the total checksum
        checksum = checksum + b_ord
    # shifts checksum 16 bits to the left or max of bList
    checksum = checksum << 16 | max(bList)
    #return the final checksum
    return checksum