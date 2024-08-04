class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display_attributes(self):
        for attr, value in self.__dict__.items():
            print(f"{attr.capitalize().replace('_', ' ')}: {value}")
        print("\n\n\n-------------------------\n")

# Creating an instance of the Student class
student1 = Student(1, "Socrates", "Philosophy 101")

# Calling the display_attributes function
print("Here's the first student: ")

student1.display_attributes()

student2 = Student(2, "Sigma Pi Theta Math", "Mathematics 303")

student2.email = "Email@com.Pi"

print("And the second student:")

student2.display_attributes()