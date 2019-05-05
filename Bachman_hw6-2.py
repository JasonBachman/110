'''
Jason Bachman
CSC 110 - Homework 6-2
Due 3/25/19
'''

def openFile():
    existingFile = False
    while existingFile == False:
        fileName = str(input("Please enter the name of the data file: "))
        try:
            gradFile = open(fileName, 'r')
            existingFile = True
        except IOError:
            print("File not found, please try again...")
    return gradFile





def dualSort(list1, list2):
    for i in range(0, len(list1)):
        min = i
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min]:
                min = j
        list1[i], list1[min] = list1[min], list1[i]
        list2[i], list2[min] = list2[min], list2[i]
    return list2, list1


def main():
    yearList, percentFemale = getData()
    yearList, percentFemale = dualSort(percentFemale, yearList)
    for i in range(len(yearList)):
        print(yearList[i], percentFemale[i])
main()




def getData():
    title_list = []
    genre_list = []
    runtime_list = []
    rating_list = []
    studio_list = []
    year_list = []
    inFile = openFile()
    line = inFile.readline()
    while line != "":
        line = inFile.readline
        line = line.strip()
        title, genre, runtime, rating, studio, year = line.split(',')
        title_list.append(title)
        genre_list.append(genre)
        runtime_list.append(runtime)
        rating_list.append(rating)
        studio_list.append(studio)
        year_list.append(year)
    inFile.close()
    return title_list, genre_list, runtime_list, rating_list, studio_list, year_list