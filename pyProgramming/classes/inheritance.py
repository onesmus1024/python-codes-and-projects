
class Room:
    def __init__(self,width,height,**kwargs):
        self.width = width
        self.height=height

    def area(self):
        area = self.width*self.height
        return area

class RoomVolume(Room):
    def __init__(self, base,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.width = args[0]
        self.height = args[1]
        self.base=base
    
    def volume(self):
        volume = self.width*self.height*self.base

        return volume



room1 = RoomVolume(20, 30,40,k=20)
print(room1.area())
print(room1.volume())

