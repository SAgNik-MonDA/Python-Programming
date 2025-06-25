class Car:
    @staticmethod
    def start():
        print("car started....")
    @staticmethod
    def stop():
        print("car stopped....")
class Toyotacar(Car):
    def __init__(self,name):
        self.name=name

car1=Toyotacar("fortuner")
car2=Toyotacar("abc")
print(car1.start())
        