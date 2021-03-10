class Swift:
    def drive(self):
        print("Driving swift car")

class Sonet:
    def drive(self):
        print("Driving sonet car")

class Person:
    def start(self,car):
        car.drive()

sw=Swift()
p=Person()
p.start(sw)
