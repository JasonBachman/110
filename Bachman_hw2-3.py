'''
Jason Bachman
CSC 110 - Homework 2 - Programming in Python
Due 2/4/19
'''
i=0  #sets i to 0
most = 0 #Sets most to 0
while i<7:    #while loop asking for the amount caught each day
    day=int(input("How many bugs did you collect on day "+str(i+1)+"? "))
    if day > most:  #keeps track of which day is the most
        most = day
    i = i+1   #increments i
print("The highest number of bugs collected this week is ",most)  #prints total
