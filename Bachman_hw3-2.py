'''
Jason Bachman
CSC 110 - Homework 3 - Programming in Python
Due 2/11/19
'''
#initializes allHeights list, i variable and, more boolean
everyotherHeight = []
allHeights = []
i = 0
more = True
#loop that runs till more = false that collects all heights only putting every other one in the list
while more == True:
    height = int(input("Enter height: "))
    allHeights.append(height)
    if height != -1:
        if i%2 == 0:
            everyotherHeight.append(height)
        i=i+1
    else:
        more = False
#prints every other height
print(everyotherHeight)
