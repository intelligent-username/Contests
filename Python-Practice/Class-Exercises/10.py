class Student:
    student_id = "123"
    student_name = "John Carter"
    """This is a student class."""

    def changer(self, str):
        self.__doc__ = str

print("Original:")
student = Student()
docs1 = []
for attribute, value in student.__dict__.items():
    if not attribute.startswith('_'):
        print(f'{attribute} -> {value}')
    else:
        docs1.append(f'{attribute} -> {value}')
print(docs1)

student.student_class = "45"
student.student_ranking = 3
student.student_name = "Smitthin Lexondint"
student.changer("aoifubeiu")  # Call the changer method on the instance

docs2 = []
print("Modified:")
for att, val in student.__dict__.items():
    if not att.startswith('_'):
        print(f'{att} -> {val}')
    else:
        docs2.append(f'{att} -> {val}')
print(docs2)

del student.student_name

print("Forgor student name")
for att, val in student.__dict__.items():
    if not att.startswith('_'):
        print(f'{att} -> {val}')

print("No garbage (docstring) values changed :)")
