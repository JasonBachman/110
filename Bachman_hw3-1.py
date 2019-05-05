'''
Jason Bachman
CSC 110 - Homework 3 - Programming in Python
Due 2/11/19
'''
#asks how many cars passed and initializes the list
carsPassed=int(input("How many cars passed the sensor? ")) 
carsSpeeds = []
#Gets all the speeds
for i in range(carsPassed):
    speed = int(input("Enter the speed for car "+str(i+1)+": "))
    carsSpeeds.append(speed)
#initializes these 2 variables
totalSpeed = 0
speeders = 0
#finds speeders
limit = int(input("Enter the speed limit: "))
for i in range(carsPassed):
    if carsSpeeds[i] > limit:
        totalSpeed = totalSpeed + carsSpeeds[i]
        speeders = speeders + 1
#Prints output

if totalSpeed == 0:
    print("There were no cars exceeding the speed limit")
else:
    averageSpeed = totalSpeed/speeders
    print("The average speed of a speeding car is ", averageSpeed)
