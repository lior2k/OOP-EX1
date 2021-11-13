import json
import csv
from mybuilding import MyBuilding
from myelevator import MyElevator
from mycall import MyCall
from mycalls import MyCalls


# def Allocate(st1 , st2 , st3 ):
#     with open(st1, 'r') as f:
#         data = json.load(f)
#     building = mybuilding()
#     elev_list = data["_elevators"]
#     for x in elev_list:
#         elevator = myelevator(x["_id"], x["_speed"], x["_minFloor"], x["_maxFloor"], x["_closeTime"], x["openTime"], x["_startTime"], x["_stopTime"])
#         building = building + elevator

# class MyElevator:
#
#     def __init__(self, id: int, speed: int, minfloor: int, maxfloor: int, closetime: int, opentime: int, starttime: int, stoptime: int):
#         self._id=id
#         self._speed=speed
#         self._minfloor=minfloor
#         self._maxfloor=maxfloor
#         self._closetime=closetime
#         self._opentime=opentime
#         self._starttime=starttime
#         self._stoptime=stoptime
#
#     def get_id(self):
#         return self.id
#
#     def get_speed(self):
#         return self._speed
#
#     def get_minfloor(self):
#         return self._minfloor
#
#     def get_maxfloor(self):
#         return self._maxfloor
#
#     def get_closetime(self):
#         return self._closetime
#
#     def get_opentime(self):
#         return self._opentime
#
#     def get_starttime(self):
#         return self._starttime
#
#     def get_stoptime(self):
#         return self._stoptime
#
#     def __str__(self):
#         return f"elevator id: {self._id} speed: +{self._speed}"
#
#     def __repr__(self):
#         return f"elevator id: {self._id} speed: +{self._speed}"

# class MyBuilding:
#
#     def __init__(self, num: int):
#         self._numberOfElevators=num
#         self._elevlist = []
#
#     def getNumberOfElevators(self):
#         return self._numberOfElevators
#
#     def __add__(self, other: MyElevator):
#         if isinstance(other, MyElevator):
#             self._elevlist.append(other)
#
#     def __str__(self):
#         return self._elevlist.__str__()




if __name__ == '__main__':
    with open("B2.json" ,'r') as f:
        data_dict = json.load(f)

    building = MyBuilding(len(data_dict["_elevators"]))
    elev_list = data_dict["_elevators"]
    for x in elev_list:
        elevator = MyElevator(x["_id"], x["_speed"], x["_minFloor"], x["_maxFloor"], x["_closeTime"], x["_openTime"],
                              x["_startTime"], x["_stopTime"])
        building + elevator

    print(building)
    all_calls = []
    with open('Calls_B.csv') as f:
        filereader = csv.reader(f)
        for row in filereader:
            all_calls.append(row)

    print(all_calls)
    my_calls = MyCalls()
    for x in all_calls:
        temp_call = MyCall(x[1], x[2], x[3])
        my_calls + temp_call

    print(my_calls)

    for call in my_calls:
        for elevator in building._elevlist:
            pass
