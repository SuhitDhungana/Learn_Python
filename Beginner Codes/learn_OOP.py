class Person:
    def __init__(self, name, age): # this method is always invoked whenever I call this class
        self.name = name
        self.age = age
        
    def info(self):
        print(f"{self.name} is {self.age} years old")
        
person1 = Person("Bikash", 15) # When this class is called, 'person1' is passed as argument in form of 'self'
person2 = Person("Anuradha", 82)
person1.info()
person2.info()
        
        