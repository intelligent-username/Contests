# Assigning Partners; IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2014/stage%201/juniorEn.pdf #5
def main1():
    print(main2())

def main2():
    N = int(input())  # Number of students in the class

    stu_1 = input().split()  # Names of N students separated by single spaces; no two students have the same name, don't even trip
    stu_2 = input().split()  # Partner of each student.

    # The student in position i in stu_1 is the partner of the student in position i in stu_2, and vice versa
    # Also, they can't partner with themselves

    pairs = set()

    for x in range(N):
        pairs.add((stu_1[x], stu_2[x]))

    pairs = list(pairs)

    for name in set(stu_1):
        counter = sum(1 for pair in pairs if pair[0] == name)
        if counter > 1:
            return "bad"

    return "good"

main1()
