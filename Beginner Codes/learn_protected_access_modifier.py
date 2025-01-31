# "Protected" means a method or attribute that is intended to be accessed by only by the
# members of it's class or subclass(es).
# It is represented by an underscore before the method/attribute 

# It is just a convention; the attribute/method, either protected or private, isn't actually
# what its meant to be. The only difference is in protected access modifier, 
# there is no "Name Mangling, but in private, there is "Name Mangling" 


class Employee:
    def __init__(self, name, id, salary):
        self._name = name
        self._id = id
        self._salary = salary
        
e1 = Employee("Oxygen", 600, 5000)
print(e1._name, e1._id, e1._salary)