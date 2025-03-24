# Static method belong to a class rather than an instance of the class (object)
# They are defined using @staticmethod decorator and doesn't require 'self,' for it doesn't 
# require an instance of class. 
# It is used to often create utility functions that doesn't need access of instances
class School:
    def __init__(self, name, classes, address):
        self.name = name
        self.classes = classes
        self.address = address
        
    def show_info(self):
        print(f"{self.name} has {self.classes} classes and is located in {self.address}")
        
    @staticmethod # doesn't work on an instance, like a typical function
    def students(student):
        stds = ("Sam", "Harry", "Joe")
        return student in stds
    
print(School.students("Harry"))
school_1 = School("James", 12, "Maine")
print(school_1.name)