from abc import ABC, abstractmethod

'''
-> The abc module stands for "Abstract Base Classes." It allows you to define abstract 
classes in Python. 
-> An abstract class is a class that cannot be instantiated on its own 
and is meant to be a blueprint for other classes.
-> ABC is a base class used to create abstract classes.
abstractmethod is a decorator that is used to declare a method as abstract. 
-> An abstract method is a method that must be overridden in any subclass.
'''
class Shapes():
    @abstractmethod
    ''' any subclass of Shapes() must implement 'area()' method, else the program
    will raise an error'''
    def area():
        pass

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14159 * (self.radius ** 2)

class Rectangle(Shapes):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
class Triangle(Shapes):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        return 0.5 * self.height * self.width

def main():
    r = float(input("Enter radius of circle: "))
    l = float(input("Enter width of rectangle: "))
    b = float(input("Enter length of rectangle: "))
    h = float(input("Enter height of triangle: "))
    w = float(input("Enter width of the triangle: "))
    shapes = (Circle(r), Rectangle(l, b), Triangle(h, w))
    for shape in shapes:
        print(f"{shape.area():.2f} cm^2")
        

if __name__ == "__main__":
    main()