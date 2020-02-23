from tspdb import TSPDatabase

#assume each location ID is on a new line
filepath = "greedy_path.txt"

db = TSPDatabase()

ridePath = list()

#open file
file = open(filepath, "r")

#loop through file and put each location in the list
for line in file:
    id=line.rstrip()
    attraction = db.get_attraction_by_id(int(id))

    if attraction is None:
        print("Attraction with ID: "+id+ " not found! Skipping...")

    elif attraction in ridePath:
        print("Attraction with ID: "+id+" already in list. Are you sure you want to duplicate? Skipping...")

    else:
        ridePath.append(attraction)

print("Proposed path is: ")

for attr in ridePath:
    print(attr.name)

#attempt to simulate path. Use basic assumptions.
date = "2018-11-01" #pick random date
walkSpeed = 1 #meters per second

#assume that already are at Acttraction Start, wait in line for Start, take the ride for Start
#and then walk Attraction End

distanceAccumulated = rideTimeAccumulated = waitTimeAccumulated = 0

for i in range(0, len(ridePath)):
    #see if we've hit the last location
    if i == len(ridePath)-1:
        print("Route Finished!")
        break

    startAttr = ridePath[i]
    endAttr = ridePath[i + 1]

    distance = db.get_attraction_distance(startAttr.id,endAttr.id)
    waitTime = db.get_wait_time(date,startAttr.id)

    #if distance is 0 meters, make it 50 meters
    if distance == 0:
        distance=50

    #if there is no wait time, assume the person spends 30 minutes there
    if waitTime is None:
        waitTime = 30

    distanceAccumulated += distance
    waitTimeAccumulated+=waitTime

    print("Riding "+startAttr.name +".\tWait takes "+str(waitTime)
          +" minutes.\t Walking to "+endAttr.name+" at distance "+str(distance)+" meters.")


walkingTime = distanceAccumulated/walkSpeed/60

print("Route totals:")
print("Walking distance: "+str(distanceAccumulated)+" meters for "+str(walkingTime/60)+" hours.")
print("Waiting in line (hours): "+str(waitTimeAccumulated/60))
print("Total park time (hours): "+ str((walkingTime+waitTimeAccumulated)/60))

open_hours = db.get_open_hours_by_date(date)

print("For "+date+" park is open "+open_hours+" hours")
