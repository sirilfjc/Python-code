#ABC = Abstract Base Class
#abstractmethod = A method that must be implemented in child classes
#Python doesn’t allow creating objects of abstract classes.

from abc import ABC, abstractmethod 
 
class Area(ABC): #base class / super class (Area is an abstract class)
 
    @abstractmethod
    def area(self): #It has an abstract method area()
        pass
#Any class that inherits Area must override this method

class Triangle(Area): #subclass
 
    # overriding abstract method
    def area(self):
        print("Triangle: my area is 1/2 * base * height")
 
class Pentagon(Area): #subclass
 
    # overriding abstract method
    def area(self):
        print("Pentagon: my area is (1/4) * √(5(5+2√5)) * side²")
 
class Hexagon(Area): #subclass
 
    # overriding abstract method
    def area(self):
        print("Hexagon: my area is (3√3/2) * side²")
 
class Quadrilateral(Area): #subclass
 
    # overriding abstract method
    def area(self):
        print("Quadrilateral: my area is length * width")
 
# Driver code for calling of methods
# Creating the objects to call the abstract method.
R = Triangle()
R.area()
 
K = Quadrilateral()
K.area()
 
R = Pentagon()
R.area()
 
K = Hexagon()
K.area()
