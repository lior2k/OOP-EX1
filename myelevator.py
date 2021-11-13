from mycall import MyCall

class MyElevator:

    def __init__(self, id: int, speed: int, minfloor: int, maxfloor: int, closetime: int, opentime: int, starttime: int, stoptime: int):
        self._id = id
        self._speed = speed
        self._minfloor = minfloor
        self._maxfloor = maxfloor
        self._closetime = closetime
        self._opentime = opentime
        self._starttime = starttime
        self._stoptime = stoptime
        self._calls = []
        self._time=0

    def get_id(self):
        return self.id

    def get_speed(self):
        return self._speed

    def get_minfloor(self):
        return self._minfloor

    def get_maxfloor(self):
        return self._maxfloor

    def get_closetime(self):
        return self._closetime

    def get_opentime(self):
        return self._opentime

    def get_starttime(self):
        return self._starttime

    def get_stoptime(self):
        return self._stoptime

    def __str__(self):
        return f"elevator id: {self._id} speed: +{self._speed}"

    def __repr__(self):
        return f"elevator id: {self._id} speed: +{self._speed}"

    def __add__(self, other):
        if isinstance(other, MyCall):
            self._calls.append(other)

    def get_calls(self):
        return self._calls


