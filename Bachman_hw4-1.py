'''
Jason Bachman
CSC 110 - Homework 4 - Working with Python Functions
Due 2/25/19
'''
#initializes the lists
artist = []
price = []
title = []
#get data function to make 3 lists. artist names, prices of the work, and  titles
def getData():
    works = int(input("How many works of art are there? "))
    #for loop that gets as many items for each list as there are works
    for i in range(works):
        artist.append(input("Enter the artists name: "))
        title.append(input("Enter the title of the piece: "))
        price.append(float(input("Enter the price of the piece: ")))
    return (artist, price, title)
#search art function asks what piece your looking for and finds the coorisponding artist name and price
def searchArt(title, price, artist):
    chosen = input("enter the name of the piece of art: ")
    if chosen in title:
        position = title.index(chosen)
        chosenArtist =  artist[position]
        chosenPrice =  price[position]
        return (chosen, chosenArtist, chosenPrice)
    else:
        -1
#returns the pertinant info
    

#average price function
def averagePrice(price):
    total = 0
    #for loop to calculate the average price of all works
    for i in range(len(price)):
        total = total + price[i]
        i+=1
    average = total/len(price)
    #returns the average price
    return (average)

#main function
def main():
    #calls get data, search art and average price functions
    getData()
    chosen, chosenArtist, chosenPrice = searchArt(title, price, artist)
    average = averagePrice(price)
    #final output
    print("the artist who painted " + str(chosen) + " is " + str(chosenArtist) + ". And the price is $" + str(chosenPrice))
    print("The average price of all artworks at the galory is $" + str(average))
