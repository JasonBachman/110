'''
Jason Bachman
CSC 110 - Homework 10
Due 4/22/19
'''

# added a gap work counter as a global variable
gapswork = 0
# Function to create a list of all ways one gap can be inserted into
# a string.  The input is a string, the output is a list of strings
# with a gap inserted into all positions of the input string

def insertOneGap(strng):
    alignments = []
    #called in gapswork
    global gapswork
    for i in range(len(strng)):
        #added 1 to the counter
        gapswork+=1
        newStrng = strng[0:i] + '-' + strng[i:len(strng)]
        alignments = alignments + [newStrng]
    alignments = alignments + [strng + '-']

    return alignments


# Function to take a set union of a pair of lists
# This is used to eliminate any duplicates in the list when they are combined
def Union(list1, list2):
    for a in list2:
        if a not in list1:
            list1 = list1 + [a]
    return list1


# Function to create all possible alignments of a string with a certain number
# of gaps inserted
def insertAllGaps(strng, gaps):
    # List of alignments starts with the initial string
    alignments = [strng]

    # Loop to insert one gap at a time
    for i in range(gaps):

        # Initialize list of new alignments with i gaps in the string
        newAlignments = []

        # For every string in the list of alignments
        for st in alignments:
            # Insert one gap in each alignment in the list
            al = insertOneGap(st)

            # Add the new alignment to the list of new alignments being created
            newAlignments = Union(newAlignments, al)

        # The alignments list now becomes the new alignments list to now
        # add another gap to each of the alignments in the new list
        alignments = newAlignments
    return alignments


# Function to print all of the alignments
# added indices which is the locations of the optimal alignments and best whcih is the optimal score
def printResults(st, alignments, comparisons, indices, best):
    print("There are ", len(alignments), " alignments")
    print("the following are optimal")
    for i in range(len(indices)):
        print(st)
        print(alignments[indices[i]])
        print("score: ", best)
        print(" ")
    print("there were ", comparisons, " comparisons")
    print("The amount of work done (gaps) ", gapswork)
#function to compare the 2 allignments and get a score.. appends every score to a list then enumerates the locations of the best scores and returns the locations and their score
def compare(st, alignments):
    score_list = []
    total = 0
    best = -10**99
    for i in range(len(alignments)):
        score = 0
        for j in range(len(st)):
            if alignments[i][j] == st[j]:
                score += 1
                total += 1
            elif alignments[i][j] == "-":
                total += 1
            elif alignments[i][j] != st[j]:
                score -= 1
                total += 1
        score_list.append(score)
        if best <= score:
            best = score
    indices = [i for i, x in enumerate(score_list) if x == best]
    return indices, best
# Main function
def main():
    # Get the two strings to align
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")

    # Compute alignments adding gaps to the shorter string
    if len(str1) > len(str2):
        longStr = str1
        shortStr = str2
    else:
        longStr = str2
        shortStr = str1
    alignments = insertAllGaps(shortStr, len(longStr) - len(shortStr))
    comparisons = len(longStr) * len(alignments)
    indices, best = compare(longStr, alignments)
    printResults(longStr, alignments, comparisons, indices, best)


main()