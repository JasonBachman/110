'''
Jason Bachman
CSC 110 - Homework 9
Due 4/15/19
'''

import queue


# Function to open the file
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter name of data file: ")
        try:
            inFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid filename, please try again ... ")
    return inFile

#gets the tslice value

def getProcs(cpuQ):
    infile = openFile()

    # reads the first line containing tslice
    line = infile.readline()

    #gets tslice value as an int
    tslice = int(line.strip())

    # loops through the list and adds the processes to the queue
    for line in infile:
        proc = line.strip()
        cpuQ.put(proc)
    infile.close()
    return tslice, cpuQ


# prints queue

def printQueue(tslice, cpuQ):
    print("The time slice is ", tslice, " \n The contents of the queue are: ")
    for i in range(cpuQ.qsize()):
        proc = cpuQ.get()
        cpuQ.put(proc)
        print(proc)


#executes processes

def scheduleProcs(tslice, cpuQ):

    while (cpuQ.empty() != True):

        #get next process
        proc = cpuQ.get()

        #get id and execution time
        PID, exectime = proc.split(",")

        #exectime to an int
        exectime = int(exectime)

        print("Getting next process - Process ", PID, " has ", exectime, " instructions to execute")

        timer = 0
        limit = tslice * 2

        if exectime <= limit:
            while (timer < tslice) and (exectime > 0):      #tests the number of executes and if thats above or below the limit it will handle it accordingly
                exectime = exectime - 1
                timer = timer + 1
                print("Executing instruction ", exectime, " of process ", PID, ".  Timer = ", timer)
        elif exectime > limit:
            newtslice = int(exectime * .2)
            while (timer < newtslice) and (exectime > 0):
                exectime = exectime - 1
                timer = timer + 1
                print("Executing instruction ", exectime, " of process ", PID, ".  Timer = ", timer)
        # If proc still has instructions to execute put it back in the queue
        if (exectime > 0):

            #updates info
            proc = PID + "," + str(exectime)

            # Put the process back in the queue
            cpuQ.put(proc)

            print("Put process ", PID, " back in queue with ", exectime, " instructions left to execute")
        else:
            print("*** Process ", PID, " Complete ***")
    return



def main():
    #gets queue
    cpuQ = queue.Queue()
    #calls processes
    tslice, cpuQ = getProcs(cpuQ)

#call print queue
    printQueue(tslice, cpuQ)



#call schedule processes
    scheduleProcs(tslice, cpuQ)

main()