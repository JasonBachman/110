'''
Jason Bachman
CSC 110 - Homework 6-1
Due 3/25/19
'''
#uses the same function we have been to check the file
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


def getData():
    # initializes lists
    yearList = []
    malePerncent = []
    femalePerncent = []
    inFile = openFile()
    line = inFile.readline()
    line = inFile.readline()
    while line != "":               #this reads and makes all the lists
        line = line.strip()
        print(line)
        year, male, female = line.split(',')
        print(male)
        yearList = yearList + [int(year)]
        malePerncent = malePerncent + [male]
        femalePerncent = femalePerncent + [female]
        line = inFile.readline()
    inFile.close()
    return yearList, malePerncent, femalePerncent


def getYearBinary(yearList, year):
    position = 0
    computations = 0
    left = 0
    right = len(yearList) - 1
    found = False
    while right >= left and found == False:
        mid = (left + right) // 2
        if yearList[mid] == year:
            found = True
            position = mid
            computations += 1
        elif yearList[mid] > year:
            right = mid - 1
            postion = right
            computations += 1
        else:

            left = mid + 1
            position = left
            computations += 1
    print("\nBinary Search made ",computations," computations")
    return position

def getYearLinear(yearList, year):
    position = 0
    i = 0
    computations = 0
    yearFound = False
    while i < len(yearList) and yearFound == False:
        computations += 1
        if yearList[i] == year:
            position = i
            yearFound = True
        i += 1
    print("\nLinear Search made ",computations," computations")
    return position



'''
The best case scenario for linear is if the desired item is first and worst case is if its last
best case for binary is if its the middle term and worst case is of it is the first or last
'''

def printResults(yearList, malePerncent, femalePerncent, index, year):
    if (year in yearList) == True:
        print("The percentage of female CS graduates in ", year, "was ", femalePerncent[index])
        print("The percentage of male CS graduates in ", year, "was ", malePerncent[index])

    else:
        print("Invalid Year")

def main():
    yearList, malePerncent, femalePerncent = getData()
    year = int(input("Enter year to search for: "))
    index = getYearBinary(yearList, year)
    getYearLinear(yearList, year)
    printResults(yearList, malePerncent, femalePerncent, index, year)
main()