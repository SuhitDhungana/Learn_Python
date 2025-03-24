class Classroom:
    def __init__(self, class_teacher, students_no, section):
        self.class_teacher = class_teacher
        self.students_no = students_no
        self.section = section
        
    @property # Getter (gets class_teacher)
    def get_class_teacher(self): 
        return self.class_teacher
    
    @get_class_teacher.setter # Setter (updates class_teacher accordingly)
    def get_class_teacher(self, new_classteacher):
        self.class_teacher = new_classteacher
        

classroom1 = Classroom("Jay", 567, "M") # Create an instance
print(classroom1.students_no)
print(classroom1.get_class_teacher) # Getter

classroom1.get_class_teacher = "Lila" # Updating the class_teacher i.e. Setter
print(classroom1.get_class_teacher)