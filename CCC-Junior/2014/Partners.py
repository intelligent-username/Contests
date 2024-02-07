# Assigning Partners; IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2014/stage%201/juniorEn.pdf #5

N = int(input()) # Number of students in the class

stu_1 = input().split() # Names of N students separated by single spaces; no two students have same name don't even trip

stu_2 = input().split() # Partner of each student. 

# The student in position i in stu_1 is the parter of the student in position i in stu_2, and vice versa
