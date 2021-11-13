class MyCall:

    def __init__(self,time: str, src: str, dest: str):
        self.time_recieved = float(time)
        self.src = int(src)
        self.dest = int(dest)
        self.allocatedto=-1

    def get_time_recieved(self):
        return self.time_recieved

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.allocatedto

    def __str__(self):
        return f"Elevator Call,{self.time_recieved},{self.src},{self.dest},{self.allocatedto},-1"

    def __repr__(self):
        return f"Elevator Call,{self.time_recieved},{self.src},{self.dest},{self.allocatedto},-1"