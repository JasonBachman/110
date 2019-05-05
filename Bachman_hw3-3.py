'''
Jason Bachman
CSC 110 - Homework 3 - Programming in Python
Due 2/11/19
'''
#initializes lists and most expensive variable
artist = []
price = []
title = []
mostExpensive = 0
#asks how many works there are
works = int(input("How many works of art are there? "))
#adds each to the apropriote list and finds the most expensive
for i in range(works):
    artist.append(input("Enter the artists name: "))
    title.append(input("Enter the title of the piece: "))
    price.append(float(input("Enter the price of the piece: ")))
    if price[i] > mostExpensive:
        mostExpensive = price[i] 
#indexs the position of the most expensive and prints all the information
position = price.index(mostExpensive)
print("The highest price item is ", title[position]," by ", artist[position]," at ", price[position])
