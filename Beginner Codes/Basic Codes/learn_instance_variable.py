class Employee:
    def __init__(self, name):
        self.name = name
        self.id = 100
        
    def show_details(self):
        print(f"The employee whos ID is {self.id} is {self.name}.")
        
e1 = Employee("Suhit") # Since in __init__, only 2 arguments (self, name) are passed, we 
                        # needn't pass the id
e1.show_details()