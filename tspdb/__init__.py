from tspdb.tspdatabase import TSPDatabase

import os

db = TSPDatabase()

filePath = os.path.abspath(__file__)

splits = os.path.split(filePath)

attractionsPath = splits[0] + os.sep + "attractions.json"

distancesPath = splits[0] + os.sep + "distances.json"

waitTimesPath = splits[0] + os.sep + "waitTimes.json"

openHoursPath = splits[0] + os.sep + "openHours.json"

db.load_attractions_from_file(attractionsPath)

db.load_distances_from_file(distancesPath)

db.load_wait_time_from_file(waitTimesPath)

db.load_open_hours_from_file(openHoursPath)