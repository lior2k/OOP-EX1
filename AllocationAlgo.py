import json
import csv
from mybuilding import MyBuilding
from myelevator import MyElevator
from mycall import MyCall
from mycalls import MyCalls

def calctime(src: int, dest: int, elevator: MyElevator):
    elevatortimes = elevator.get_opentime()+elevator.get_closetime()+elevator.get_starttime()+elevator.get_starttime()
    return abs(src-dest)/elevator.get_speed()+2*elevatortimes

def isinpath(call, nextcall, elevator):
    if nextcall.time_recieved-call.time_recieved < calctime(call.get_src(), nextcall.get_src(), elevator):
        return True
    return False

# def Allocate(st1 , st2 , st3 ):
#     with open(st1, 'r') as f:
#         data = json.load(f)
#     building = mybuilding()
#     elev_list = data["_elevators"]
#     for x in elev_list:
#         elevator = myelevator(x["_id"], x["_speed"], x["_minFloor"], x["_maxFloor"], x["_closeTime"], x["openTime"], x["_startTime"], x["_stopTime"])
#         building = building + elevator

if __name__ == '__main__':
    with open("B5.json", 'r') as f:
        data_dict = json.load(f)

    building = MyBuilding(len(data_dict["_elevators"]))
    elev_list = data_dict["_elevators"]
    for x in elev_list:
        elevator = MyElevator(x["_id"], x["_speed"], x["_minFloor"], x["_maxFloor"], x["_closeTime"], x["_openTime"],
                              x["_startTime"], x["_stopTime"])
        building + elevator

    print(building)
    all_calls = [] #list of lists of calls as strings
    with open('Calls_B.csv') as f:
        filereader = csv.reader(f)
        for row in filereader:
            all_calls.append(row)

    print(all_calls)
    my_calls = MyCalls() #list of calls
    for x in all_calls:
        temp_call = MyCall(x[1], x[2], x[3])
        my_calls + temp_call

    print(my_calls)

    for call in my_calls.list_of_calls:  #allocation start
        numofcall = 10000
        elev_id = 0
        if (call.allocatedto == -1):
            for elevator in building._elevlist:
                if numofcall > len(elevator.get_calls()):
                    numofcall = len(elevator.get_calls())
                    elev_id = elevator._id
            curr_elev = building._elevlist[elev_id]
            call.allocatedto = elev_id
            curr_elev + call
            temp_call_index = my_calls.get_next_index(call)
            if temp_call_index != -1 and temp_call_index < len(my_calls.list_of_calls):
                temp_call = my_calls.list_of_calls[temp_call_index]
                time = calctime(call.get_src(), call.get_dest(), curr_elev)
                dir = call.get_dir()
                while temp_call.time_recieved < call.time_recieved + time and temp_call_index < len(
                        my_calls.list_of_calls):
                    if dir == 1:
                        if temp_call.get_dir() == 1 and temp_call.allocatedto == -1:
                            if isinpath(call, temp_call, curr_elev):
                                temp_call.allocatedto == elev_id
                                curr_elev + temp_call
                    if dir == -1:
                        if temp_call.get_dir() == -1 and temp_call.allocatedto == -1:
                            if isinpath(call, temp_call, curr_elev):
                                temp_call.allocatedto == elev_id
                                curr_elev + temp_call
                    temp_call = my_calls.list_of_calls[temp_call_index]
                    temp_call_index += 1


    print(my_calls)
    print(len(building._elevlist[0]._calls))
    print(len(building._elevlist[1]._calls))
    print(len(building._elevlist[2]._calls))
    print(len(building._elevlist[3]._calls))
    print(len(building._elevlist[4]._calls))
    print(len(building._elevlist[5]._calls))
    print(len(building._elevlist[6]._calls))
    print(len(building._elevlist[7]._calls))
    print(len(building._elevlist[8]._calls))
    print(len(building._elevlist[9]._calls))
