'''
Jason Bachman
CSC 110 - Movie Data
Due 4/30/19
'''




#opens file and check to see validity
def openFile():
    existingFile = False
    while existingFile == False:
        fileName = str(input("Please enter the name of the data file: "))
        try:
            movies_file = open(fileName, "r")
            existingFile = True
        except IOError:
            print("File not found, please try again...")
    return movies_file

#get data function
def getData():
    #initializes all required lists and variables
    title_list = []
    genre_list = []
    runtime_list = []
    rating_list = []
    studio_list = []
    year_list = []
    index_list = []
    i = 0
    #opens file
    inFile = openFile()
    #reads first line to rid of headers
    line = inFile.readline()
    #reads through file assigning values to their appropriate lists
    for line in inFile:
        line = line.strip()
        title, genre, runtime, rating, studio, year = line.split(',')
        title_list.append(title)
        genre_list.append(genre)
        runtime = int(runtime)
        runtime_list.append(runtime)
        rating_list.append(rating)
        studio_list.append(studio)
        year = int(year)
        year_list.append(year)
        index_list.append(i)
        i +=1
    inFile.close()
    return title_list, genre_list, runtime_list, rating_list, studio_list, year_list, index_list

#genre search function
def genreSearch(title_list, genre_list, runtime_list, rating_list, studio_list, year_list):
    #loop to ensure valid inputs
    go = False
    while not go:
        genre = input("What genre would you like to search for: ")
        if genre in genre_list:
            go = True
        else:
            print("Invalid genre please try again...")
    #initialize needed lists
    genre_title_list = []
    genre_genre_list = []
    genre_runtime_list = []
    genre_rating_list = []
    genre_studio_list = []
    genre_year_list = []
    #loop through appending values to their lists
    for i in range(len(genre_list)):
        if genre == genre_list[i]:
            genre_title_list.append(title_list[i])
            genre_genre_list.append(genre_list[i])
            runtime = str(runtime_list[i])
            genre_runtime_list.append(runtime)
            genre_rating_list.append(rating_list[i])
            genre_studio_list.append(studio_list[i])
            year = str(year_list[i])
            genre_year_list.append(year)
    #prints well spaced resutlts
    print("TITLE".ljust(50) + "GENRE".ljust(20) + "RUNTIME".ljust(10) + "RATING".ljust(10) + "STUDIO".ljust(30) + "YEAR".ljust(40) + '\n')
    for i in range(len(genre_title_list)):
        print(genre_title_list[i].ljust(50) + genre_genre_list[i].ljust(20) + genre_runtime_list[i].ljust(10) +
              genre_rating_list[i].ljust(10) + genre_studio_list[i].ljust(30) + genre_year_list[i].ljust(40) + '\n')


#rating search
def ratingSearch(title_list, genre_list, runtime_list, rating_list, studio_list, year_list):
    #loop to ensure valid inputs
    go = False
    while not go:
        rating = input("What Rating would you like to search for: ")
        if rating in rating_list:
            go = True
        else:
            print("Invalid rating please try again...")
    # initialize needed lists
    rating_title_list = []
    rating_genre_list = []
    rating_runtime_list = []
    rating_rating_list = []
    rating_studio_list = []
    rating_year_list = []
    #loop through appending values to their lists

    for i in range(len(rating_list)):
        if rating == rating_list[i]:
            rating_title_list.append(title_list[i])
            rating_genre_list.append(genre_list[i])
            runtime = str(runtime_list[i])
            rating_runtime_list.append(runtime)
            rating = str(rating_list[i])
            rating_rating_list.append(rating)
            rating_studio_list.append(studio_list[i])
            year = str(year_list[i])
            rating_year_list.append(year)
    #prionts well spaced results to query
    print("TITLE".ljust(50) + "GENRE".ljust(30) + "RUNTIME".ljust(10) + "RATING".ljust(10) + "STUDIO".ljust(30) + "YEAR".ljust(40) + '\n')

    for i in range(len(rating_title_list)):
        print(rating_title_list[i].ljust(50) + rating_genre_list[i].ljust(30) + rating_runtime_list[i].ljust(10) +
              rating_rating_list[i].ljust(10) + rating_studio_list[i].ljust(30) + rating_year_list[i].ljust(40) + '\n')

#longest searched
def longestByStudio(title_list, genre_list, runtime_list, rating_list, studio_list, year_list):
    #ensures valid input
    go = False
    while not go:
        studio = input("What Studio would you like to know the longest film of: ")
        if studio in studio_list:
            go = True
        else:
            print("Invalid studio please try again...")
    longest = 0
    pos = 0

    #finds the longest film then catologs its position then gets all coorosponding info
    for i in range(len(studio_list)):
        if studio == studio_list[i] and longest < runtime_list[i]:
            longest = runtime_list[i]
            pos = i
    longest_title = title_list[pos]
    longest_genre = genre_list[pos]
    longest_runtime = str(runtime_list[pos])
    longest_rating = rating_list[pos]
    longest_studio = studio_list[pos]
    longest_year = str(year_list[pos])
    #prints results
    print("TITLE".ljust(60) + "GENRE".ljust(30) + "RUNTIME".ljust(10) + "RATING".ljust(10) + "STUDIO".ljust(30) + "YEAR".ljust(40) + '\n')
    print(longest_title.ljust(60), longest_genre.ljust(30), longest_runtime.ljust(10), longest_rating.ljust(10), longest_studio.ljust(30), longest_year.ljust(40))

#title search
def title_search(title_list, genre_list, runtime_list, rating_list, studio_list, year_list):
    #ensures valid input
    go = False
    while not go:
        title = input("Enter title: ")
        if title in title_list:
            go = True
        else:
            print("Invalid title please try again...")
    i = 0
    #loops through list looking for title that was searched catologs position
    found = False
    while i < len(title_list) and found == False:
        if title_list[i] == title:
            found = True
            pos = i
        else:
            i = i + 1
    #adds it all to appropriate list
    searched_title = title_list[pos]
    searched_genre = genre_list[pos]
    searched_runtime = str(runtime_list[pos])
    searched_rating = rating_list[pos]
    searched_studio = studio_list[pos]
    searched_year = str(year_list[pos])
    #prints results
    print("TITLE".ljust(40) + "GENRE".ljust(30) + "RUNTIME".ljust(20) + "RATING".ljust(20) + "STUDIO".ljust(30) + "YEAR".ljust(40) + '\n')
    print(searched_title.ljust(40), searched_genre.ljust(30), searched_runtime.ljust(20), searched_rating.ljust(20), searched_studio.ljust(30), searched_year.ljust(40))


def average_years(year_list, runtime_list):
    total = 0
    movies = 0
    #ensures valid input
    go = False
    while go == False:
        year1 = input("Enter the range to search, (oldest first)" + '\n' + "Year 1: ")
        try:
            year1 = int(year1)
        except ValueError:
            print("please enter a valid year")
        if year1 in year_list:
            year2 = input("Year 2: ")
            try:
                year2 = int(year2)
            except ValueError:
                print("please enter a valid year")
            if year2 in year_list and year2 > year1:
                go = True
            else:
                print("invalid year parameters entered please try again.")
        else:
            print("please enter a year within the range")



    # finds all films made in a certain year range and keeps track to how many it adds then devides total runtime by number of movies to get average.
    for i in range(len(runtime_list)):
        if year_list[i] <= year2 and year_list[i] >= year1:
            total += runtime_list[i]
            movies += 1
    average = total / movies
    year2 = str(year2)
    year1 = str(year1)
    #controls the number of decimals
    "{:.2f}".format(average)
    #prints
    print("The average runtime of movies made between " + year1 + " and " + year2 + " is " + "{:.1f}".format(average))


#sort by runtime
def sort_runtime(title_list, genre_list, runtime_list, rating_list, studio_list, year_list, index_list):
    #initializes needed variables and lists
    i = 0
    j = 0
    longest = 1000000
    sorted_runtime_list = []
    sorted_index_list = []
    #loops through the runtime list over and over pulling out the longest runtime and its position and appends those to lists and assigns the coorosponding info for that position later
    while len(runtime_list) > 0:
        while i < len(runtime_list):
            if runtime_list[i] < longest:
                longest = runtime_list[i]
                j = i
                i += 1
            else:
                i += 1
        #adds all the appropriate info in the correct order
        long = runtime_list[j]
        index = index_list.pop(j)
        sorted_index_list.append(index)
        runtime_list.remove(long)
        sorted_runtime_list.append(long)
        i =0
        longest = 1000
    l = 0
    #asked for the name of the output file
    output_file = str(input("Please enter the name of the output file: "))
    #tells the program to write to the file
    sorted_data = open(output_file, 'w')
    #headers
    sorted_data.write("TITLE".ljust(70) + "GENRE".ljust(30) + "RUNTIME".ljust(20) + "RATING".ljust(20) + "STUDIO".ljust(30) + "YEAR".ljust(40) + '\n')
    #puts the correct datafrom the right spot into the new file
    while l < len(sorted_index_list):
        pos = sorted_index_list[l]
        title = str(title_list[pos])
        genre = str(genre_list[pos])
        runtime = str(sorted_runtime_list[l])
        rating = str(rating_list[pos])
        studio = str(studio_list[pos])
        year = str(year_list[pos])
        sorted_data.write(title.ljust(70) + " " + genre.ljust(30) + " " + runtime.ljust(20) + " " + rating.ljust(20) + " " + studio.ljust(30) + " " + year.ljust(40) + '\n')
        l += 1





def main():
    #calls get data and has all the lists
    title_list, genre_list, runtime_list, rating_list, studio_list, year_list, index_list = getData()
    go = False
    #while loop that lets the user ask as many questions as they want from the list presented to them
    while go == False:
        choice = input('\n'"Please choose one of the following options" + '\n'
                       "1 -- Find all the films of a certain genre" + '\n'
                       "2 -- Find all films with a certain rating" + '\n'
                       "3 -- Find the longest film made by a specific studio" + '\n'
                       "4 -- Search for a film by title" + '\n'
                       "5 -- Find average runtime of films made within a given year range" + '\n'
                       "6 -- Sort all lists by runtime and write the results to a new file" + '\n'
                       "7 -- Quit" + '\n'
                       "Choice ==> ")
        #based on the choice they select it calls the apropriote function and prints the result before asking what they would like to do next
        if choice == "1":
            genreSearch(title_list, genre_list, runtime_list, rating_list, studio_list, year_list)
        elif choice == "2":
            ratingSearch(title_list, genre_list, runtime_list, rating_list, studio_list, year_list)
        elif choice == "3":
            longestByStudio(title_list, genre_list, runtime_list, rating_list, studio_list, year_list)
        elif choice == "4":
            title_search(title_list, genre_list, runtime_list, rating_list, studio_list, year_list)
        elif choice == "5":
            average_years(year_list, runtime_list)
        elif choice == "6":
            sort_runtime(title_list, genre_list, runtime_list, rating_list, studio_list, year_list, index_list)
        #exits the loop and stops the program
        elif choice == "7":
            go = True
        #if an entry doesnt have a function it asks again
        else:
            print("please enter a valid option")
main()