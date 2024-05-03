class Student:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Marks:
    def __init__(self, a):
        self.a = a
    def average(marks):
        return sum(marks)/len(marks)

stud = Student(2, 3, 4)
classs = Marks(5)

print("Is stud an instance of 'Student': ", isinstance(stud, Student))
print("Is classs an instance of 'Marks': ",isinstance(classs, Marks))

print("Are Marks and Students subclasses of 'object' ", issubclass(Student, object), issubclass(Marks, object))
