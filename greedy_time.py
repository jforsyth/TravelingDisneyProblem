from tspdb import TSPDatabase
import sys
''''
This is an implementation of a greedy search algorithms that navigates around the park selecting the closest ride first.
The output of the algorithm is a list of attraction IDs that can be sent to the validator.py function to determine the
performance metrics of this approach. The algorithm takes as input a particular date of the year and an initial starting
attraction from which to begin its search.
'''


def find_soonest_attraction(current, neighbors:list, date:str):
    local_db = TSPDatabase()
    walking_speed = 1 # Assume 1 m/s walking speed

    closest_id=None
    min_time = sys.maxsize
    local_db = TSPDatabase()
    for target in neighbors:
        distance = local_db.get_attraction_distance(current.id,target.id)
        wait_time = local_db.get_wait_time(date,target.id)

        to_time_attraction = (distance / walking_speed) + int(wait_time)
        if to_time_attraction < min_time:
            min_time=to_time_attraction
            closest_id=target

    return closest_id


#create an instantiation of the database
db = TSPDatabase()

#select an initial attraction on which to begin the search
initial_attraction = 33

#select an initial date on which to perform the search
starting_date = "2018-09-01"

#create two lists to hold the visited and un-visited attractions
not_visited_list = db.get_attractions_list()
visited_list = list()

#record our "current" attraction and the one will we visit next
next_attraction = 0
current_attraction = db.get_attraction_by_id(initial_attraction)

while len(not_visited_list)>0:
    #mark the current attraction as visited
    visited_list.append(current_attraction)

    #remove the current attarction from the not visited lsit
    not_visited_list.remove(current_attraction)

    #find attraction that we can get into the soonest
    next_attraction = find_soonest_attraction(current_attraction, not_visited_list, starting_date)

    #set next attraction as current
    current_attraction=next_attraction

#print out the list of attractions in order starting with the initial one
for attr in visited_list:
    print(str(attr.id) + " " + attr.name)

file = open("greedy_path.txt","w")
for attr in visited_list:
    file.write(str(attr.id)+'\n')
file.close()