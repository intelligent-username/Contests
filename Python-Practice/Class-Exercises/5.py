def Student(Grade, Name, Age, Gender, School, Class, Address, Phone, Email, Parent, EMail, Number, Income, Likeable):
    return f'Grade: {Grade}, Name: {Name}, Age: {Age}, Gender: {Gender}, School: {School}, Class: {Class}, Address: {Address}, Phone: {Phone}, Email: {Email}, Parent: {Parent}, E-mail: {EMail}, Number: {Number}, Income: {Income}, Likeable: {Likeable}'
information = Student(12, "Jaileen", 17, "Female", "Big Ups School", "12th", "1234 Main St.", "416-882-7919", "jaileen@BUS.com", "Mrs. Parent", "smith@bus.com", "123-456-7890", "$500", False)
print("Student private information (DO NOT PRINT):\n", information)