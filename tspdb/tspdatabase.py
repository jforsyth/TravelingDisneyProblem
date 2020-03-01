import pickle
import json
'''

'''

#define some helper functions
def saveWithPickle(fileName, obj):
    file = open(fileName,"w")
    pickle.dump(obj,file)
    file.close()

def saveWithJSON(fileName, obj):
    file = open(fileName,"w")
    json.dump(obj,file)
    file.close()

def loadWithPickle(fileName):
    file = open(fileName,"r")
    obj =  pickle.load(file)
    file.close()
    return obj

def loadWithJSON(fileName):
    file = open(fileName,"r")
    obj = json.load(file)
    file.close()
    return obj


class Attraction:
    def __init__(self, _name:str, _id:int):
        self.name = _name
        self.id = _id


class TSPDatabase:

    attractions = list()
    distancesDict = dict()
    waitTimeDict = dict()
    openHoursDict = dict()

    #load a list of attractions from a JSON file specified as a string with an absolute path
    def load_attractions_from_file(self, filename:str):
        data = loadWithJSON(filename)

        for item in data:
            var = Attraction(item['name'], item['id'])
            TSPDatabase.attractions.append(var)

    #return a list of attractions
    def get_attractions_list(self):
        return TSPDatabase.attractions

    #load distances from a JSON file specified as a string with an absolute path
    def load_distances_from_file(self, filename:str):
        data = loadWithJSON(filename)
        TSPDatabase.distancesDict=data

    #get the distance in meters between two attractions, each specified by their attraction ID (int)
    def get_attraction_distance(self, id1:int, id2:int):
        key = str(id1)+","+str(id2)
        return TSPDatabase.distancesDict[key]

    #return the name of an attraction as a string when specified by an attraction ID (int)
    def get_attraction_name(self,id:int):
        return self.get_attraction_by_id(id).name

    #return an Attraction object for a provided attriction ID (int)
    def get_attraction_by_id(self,id:int):
        for attr in TSPDatabase.attractions:
            if attr.id == id:
                return attr
        return None

    #load wait times from a JSON file specified as a string with an absolute path
    def load_wait_time_from_file(self, filename:str):
        data = loadWithJSON(filename)
        TSPDatabase.waitTimeDict=data

    #get the wait time (minutes) for an attraction ID (int) on a given date (string formated as YYYY-MM-DD)
    def get_wait_time(self, date:str, id:int):
        day_wait_time = TSPDatabase.waitTimeDict[date]
        ride_wait_time = day_wait_time[str(id)]

        if ride_wait_time == None:
            return 0
        else:
            return ride_wait_time

    # load wait times from a JSON file specified as a string with an absolute path
    def load_open_hours_from_file(self, filename: str):
        data = loadWithJSON(filename)
        TSPDatabase.openHoursDict = data

    # get the park's open hours
    def get_open_hours_by_date(self, date: str):
        # TODO: Fix situation where total hours may be negative if open past midnight
        return TSPDatabase.openHoursDict[date]

