class Student:
    school = "ABC Academy"

    def __init__(self, name, grade):
        self.name = name
        self.grade = [grade]
    
    def grade_changer(self, grade):
        self.grade.append(grade)
    
    def name_changer(self, name):
        self.name = name

Jimmy = Student("Jimmy", "95")

print("Jimmy's profile:", Jimmy)
print("Jimmy's Grades:", Jimmy.grade)

Jimmy.grade_changer("22")

Jimmy.name_changer("Jimmy Peter")  
print("Jimmy's profile updated:", Jimmy)
print("Jimmy's Grades updated:", Jimmy.grade)

setattr(Student, "school", "ABCDEF Collegiate")
print("School name:", Jimmy.school)