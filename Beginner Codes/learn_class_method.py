class School():
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa, grade):
        self.name = name
        self.gpa = gpa
        self.grade = grade
        School.count += 1
        School.total_gpa += self.gpa
        
    @classmethod
    def average_gpa(cls):
        return School.total_gpa / School.count

student_1 = School("James", 3.4, 12)
student_2 = School("Joe", 2.2, 11)
print(f"{student_1.name}'s GPA is {student_1.gpa}.")
print(f"{student_2.name}'s GPA is {student_2.gpa}.")
print(School.average_gpa())