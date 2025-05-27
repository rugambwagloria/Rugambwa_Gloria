#import the ABC and the abstract method from the abc module
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass#this method start_ebgine has no implementation, it is an abstract method

    @abstractmethod
    def stop_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
    
    def stop_engine(self):
        print("Car engine stopped")
        
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")
    
    def stop_engine(self):
        print("Motorcycle engine stopped")
        
        #NOTES
# Abstract classes cannot be instantiated directly.we cannott create objects of abstract classes.because this would raise an error.
# They are meant to be subclassed, and the subclasses must implement the abstract methods.
# Abstract methods are defined using the @abstractmethod decorator, and they must be implemented in any subclass.

car1 = Car()
Motorcycle1 = Motorcycle()
car1.start_engine()  # Output: Car engine started
Motorcycle1.stop_engine()  # Output: Motorcycle engine started
#excerse  submit your work on github for method overriding,method overloading and method Resolution Order.USe two real world examples for the above.