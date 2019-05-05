'''
Jason Bachman
CSC 110 - Homework 5 - Working with Files
Due 3/4/19
'''

#Checks to see if the file entered is valid
def openFile():
    goodFile = False;
    while goodFile == False:
        fname = input("Enter name of data file: ")
        try:
            yearFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid filename, please try again...")
    return yearFile

#getData sorts all the information from the file into 4 lists

def getData():
    yearList = []
    totalList = []
    maleList = []
    femaleList = []
    yearFile = openFile()
    line = yearFile.readline()
    for line in yearFile:               #reads through the file
        print(line)
        year,total, male, female = line.split(',')    #splits data based on ","
        year = int(year)
        total = int(total)      #makes these values integers
        male = int(male)
        female = int(female)
        yearList.append(year)           #adds each value to the apropriate list
        totalList.append(total)
        maleList.append(male)
        femaleList.append(female)
    yearFile.close()
    return yearList, totalList, maleList, femaleList        #returns the 4 lists


#Gets the start and end year for the comparison and makes sure all the values entered are valid
def getYears():
    good = False
    keepGoing = False
    goOn = False            #these work as checkpoints
    while good == False:
        try:
            startYear = int(input("Enter a year: "))
            goOn = True
        except ValueError:              #if a bad value is entered this returns the warning
            print("please enter an actual number")
            goOn = False
        if (startYear > 2011 or startYear < 1971)and goOn:     #checks if the year is in range
            print("please enter a valid year")
        else:                                                       #same but for endyear
            try:
                endYear = int(input("Enter a year: "))
                keepGoing = True
            except ValueError:
                print("please enter an actual number")
            if startYear >= endYear:
                print("Year 2 should be after Year 1 please try again...")
            else:
                good = True                                                     #exits the loop and returns the 2 values
    return startYear, endYear



#calculates the percent changes
def computePercentChange(startYear, endYear, yearList, totalList, maleList, femaleList):
    '''
    this code does the same as the sequential search below
    start = yearList.index(startYear)
    stop = yearList.index(endYear)
    '''

    #Finds the positions in the list of start and end years
    i = 0
    found = False
    while i < len(yearList) and found == False:
        if yearList[i] == startYear:
            found = True
        else:
            i = i + 1
    start = i
    i = 0
    found = False
    while i < len(yearList) and found == False:
        if yearList[i] == endYear:
            found = True
        else:
            i = i + 1
    stop = i
    #does all the calculations to find the change in percent form
    maleChange = maleList[stop] / maleList[start]
    maleChange = maleChange - 1
    malePercent = maleChange*100
    femaleChange = femaleList[stop] / femaleList[start]
    femaleChange = femaleChange - 1
    femalePercent = femaleChange*100
    totalChange = totalList[stop] / totalList[start]
    totalChange = totalChange - 1
    totalPercent = totalChange*100
    #returns the four change percentages
    return malePercent, femalePercent, totalPercent



#Prints the results
def printResults(malePercent, femalePercent, totalPercent):
    print("The percent change overall: " + "{:.2f}".format(totalPercent)+"%")  #prints results and makes it so they are only 2 decimals
    print("The percent change male: " + "{:.2f}".format(malePercent)+"%")
    print("The percent change female: " + "{:.2f}".format(femalePercent)+"%")




#puts the year and the percent change of female graduation into a new file
def femaleData(yearList,femaleList):
    femaleGraduates = open("fmchange.txt",'w')
    i=1
    while i < len(yearList):
        change = femaleList[i]/femaleList[i-1]
        change -= 1
        change *= 100
        #this writes all the lines into the new file with \n on the end to make them all on their own line.
        femaleGraduates.write(str(yearList[i])+ " " + str(change) + '\n')
        i+=1



#main executes all the other functions with appropriote variables
def main():
    yearList, totalList, maleList, femaleList = getData()
    startYear, endYear = getYears()
    malePercent, femalePercent, totalPercent = computePercentChange(startYear,endYear,yearList, totalList, maleList, femaleList)
    printResults(malePercent, femalePercent, totalPercent)
    femaleData(yearList, femaleList)


#this is so i can just hit run and not have to type main() into the idle every time
main()
