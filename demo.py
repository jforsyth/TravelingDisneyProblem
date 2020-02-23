'''
This demo shows how to access the database and make information about attraction names, ride times, and distances between
pairs of attractions.
'''
from tspdb import TSPDatabase

#create an instance of the database. This will self-initialize itself
db = TSPDatabase()

#print out all attractions
print('Printing out all attraction names and ID numbers:')

#iterate through the list of attractions. The list contains a set of 'Attraction' objects that
#encapsulate the attraction's name (string) and identification number (int) within the system.
for attr in db.get_attractions_list():
    print(str(attr.id)+" "+attr.name)

#Within the database there is an estimate for the distance (in meters) between each attraction at the Magic Kingdom.
#This distance can be found through a look up using the attraction's identifier.
print("Attempting to find the distance between "+db.get_attraction_name(4)+" and "+db.get_attraction_name(16))

distance = db.get_attraction_distance(4,16)

print("Distance is "+str(distance)+" meters")


