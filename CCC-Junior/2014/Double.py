# DOUBLE DICE: IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2014/stage%201/juniorEn.pdf #3

p1 = 100
p2 = 100

N = int(input())
rolls = []

for _ in range(N):
    rolls += map(int, input().split())

for x in range(0, len(rolls), 2):
    if rolls[x] > rolls[x + 1]:
        p2 -= rolls[x]
    elif rolls[x] < rolls[x + 1]:
        p1 -= rolls[x + 1]

print(p1)
print(p2)

