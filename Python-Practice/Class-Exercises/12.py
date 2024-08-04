class Student:
    def __init__(self, student_id, name, major, year, gpa):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.year = year
        self.gpa = gpa
        self.courses = []
        self.grades = []

    def enroll(self, course):
        self.courses.append(course)

    def update_gpa(self, new_grade):
        if new_grade is not None:
            self.grades.append(new_grade)
            total_grades = sum(self.grades)
            num_grades = len(self.grades)
            self.gpa = total_grades / num_grades

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Major: {self.major}")
        print(f"Year: {self.year}")
        print(f"GPA: {self.gpa:.2f}")
        print("Enrolled Courses:")
        for course in self.courses:
            print(f"- {course}")

# Create an instance of the Student class
Socrates = Student(1001, "Socrates", "Philosophy", "Senior", 3.8)
Socrates.enroll("Ethics")
Socrates.enroll("Metaphysics")
Socrates.enroll("Ancient Greek Literature")

# Update GPA with new grades
Socrates.update_gpa(90)
Socrates.update_gpa(85)
Socrates.update_gpa(92)

# Display information for the student
Socrates.display_info()
Socrates.enroll("Political Science")

print("Socrates took a political science class")

Socrates.update_gpa(75)
print("Unfortunately he got a 75%, and his new GPA is " + str(Socrates.gpa))

print("\n\n--------------------\n------------------\n")

print("Meanwhile, Jimmy here is taking all of the same courses. Here are his statistics")

Jimmy = Student(2002, "Jimmy Theodore Roosevelt", "Philosophy", "Senior", 4.0)

Jimmy.enroll("Ethics")
Jimmy.enroll("Metaphysics")
Jimmy.enroll("Ancient Greek Literature")
Jimmy.enroll("Political Science")
Jimmy.update_gpa(94)
Jimmy.update_gpa(96)
Jimmy.update_gpa(95)
Jimmy.update_gpa(99)

Jimmy.display_info()
