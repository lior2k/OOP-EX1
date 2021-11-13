from mycall import MyCall

class MyCalls:

    def __init__(self):
        self.list_of_calls = []

    def __add__(self, other):
        if isinstance(other, MyCall):
            self.list_of_calls.append(other)

    def __str__(self):
        return self.list_of_calls.__str__()