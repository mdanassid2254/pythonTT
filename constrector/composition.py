#composition
class Room:
    pass
class Building:
    def __init__(self,room_count):
        self.rooms=[]
        for i in range(0,room_count):
            r=Room()
            self.rooms.append(r)
    def __del__(self):
        print("All room destroyed")
        del self.rooms
b=Building(3)
del (b)