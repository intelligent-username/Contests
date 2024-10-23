# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age

from datetime import date

class person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def age(self):
        today = date.today()

        age = today.year - self.dob.year

        if today < date(today.year, self.dob.month, self.dob.day): age -=1

        return age

name = input("Enter name: ")
country = input("Enter country of origin: ")
dob = date(int(input("Enter year of birth: ")), int(input("Enter month of birth: ")), int(input("Enter day of birth: ")))
example = person(name, country, dob)

print("Age:", example.age())
