class Employee:
    def __init__(self, name, id, salary):
        self.__name = name # Dunder before variable implies private access modifier
        self.__id = id
        self.__salary = salary
        
e1 = Employee("Hydrogen", 500, 60000)
print(e1._Employee__name, e1._Employee__id, e1._Employee__salary) # Name mangling (look it up once)
print(e1.__dir__()) # Returns object's methods and attributes

