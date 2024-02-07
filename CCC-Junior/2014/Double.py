# DOUBLE DICE: IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2014/stage%201/juniorEn.pdf #3

p1 = 100
p2 = 100

N = int(input())
rolls = []

for x in range(N):
    rolls += input().split()

for x in range(0, len(rolls), 2):
    print(x)
    if int(rolls[2*x]) > int(rolls[(2*x)+1]):
        p2 -= int(rolls[(2*x)])
    elif int(rolls[2*x]) < int(rolls[(2*x)+1]):
        p1 -= int(rolls[(2*x)+1])

print(p1)
print(p2)
