'''
Jason Bachman
CSC 110 - Homework 2 - Programming in Python
Due 2/4/19
'''
#sets i and total to 0
i = 0
total = 0
#while loop based on i
while i<9:
    score=int(input("Enter score: "))  #enter score
    total = score + total   #adds score to total
    i=i+1
average=total/9 #calculate average
print("Your average score for three weeks is: ",average)  #Prints average
