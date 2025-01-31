class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
        
    def display(self):
        print(f"The name of the person with id {self.id} is {self.name}.")
      
        
class Manager(Employee): # Inherits the properties of "Employee" within "Manager"
    def __init__(self, name, id, salary):
        super().__init__(name, id, salary) # Learn about the function of super()
        
    def salary_know(self):
        print(f"The salary of {self.name} is {self.salary}.")
        

e1 = Employee("Hydrogen", 500, 6000)
e2 = Manager("Oxyen", 600, 50000)
e1.display()
e2.salary_know()
    
    
        