class School:
    def __init__(self, name, classes, address):
        self.name = name
        self.classes = classes
        self.address = address
        
    def show_info(self):
        print(f"{self.name} has {self.classes} classes and is located in {self.address}")
        
    @staticmethod
    def students(student):
        stds = ("Sam", "Harry", "Joe")
        return student in stds
    
print(School.students("James"))
school_1 = School("James", 12, "Maine")
print(school_1.name)