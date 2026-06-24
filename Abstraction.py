"""#1.ABSTACTION:

from abc import ABC,abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return ("Car engine started...")

class Motorcycle(Vehicle):
    def start_engine(self):
        return ("Motorcycle engine started...")
    
my_car = Car()
my_bike = Motorcycle()

print(my_car.start_engine())    
print(my_bike.start_engine())"""



"""#2.ABSTRACTION:

from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def vehicle_type(self):
        pass

class truck(vehicle):
    def vehicle_type(self):
        return ("RUNS WITH DIESEL...")

class bike(vehicle):
    def vehicle_type(self):
        return ("RUNS WITH PETROL OR ELECTIC...")
    
my_truck = truck()
my_bike = bike()


print(my_truck.vehicle_type())    
print(my_bike.vehicle_type())"""


    
    










    

    





    
    






















