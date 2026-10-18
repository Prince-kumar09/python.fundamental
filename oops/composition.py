
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")

car1 = Car()
car1.start_car()



class Battery:
    def charger(self):
        print("Battery is charging")

class Mobile:
    def __init__(self):
        self.battery = Battery()

    def charge_mobile(self):
        self.battery.charger()

m1 = Mobile()
m1.charge_mobile()
