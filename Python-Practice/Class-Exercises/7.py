class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

print(type(student))
print(student.__dict__.keys())
print(student.__module__)
