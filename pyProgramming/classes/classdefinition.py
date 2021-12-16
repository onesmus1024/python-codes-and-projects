

class Car:
    def __init__(self,type,millage):
        self.type = type
        self.millage = millage
    def __hour_travelled__(self):
        hour = self.millage*10

        return hour



car1 = Car("nissan", 100)
print(car1.__hour_travelled__())