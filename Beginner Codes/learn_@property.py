class Car:
    def __init__(self, name, color, year):
        self._name = name
        self._color = color
        self._year = year
    
    @property
    def name(self):
        print(f"{self._name}")
    
    @property
    def color(self):
        print(f"The color of car is {self._color}")
    
    @name.setter    
    def name(self, new_name):
        if new_name == self._name:
            self._name = new_name
        else:
            print(f"The new name isn't the same as the old name {new_name}")
        
    
car1 = Car("Toyota", "Red", 2051)
car1.name = "Honda"
car1.name
