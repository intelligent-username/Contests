# COMPUTER PURCHASE: COMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2010/stage1/seniorEn.pdf #1

# 2*R  + 3*S + D

n = int(input(""))

lists = []
scores = {}

for x in range(n):
    lists.append(input().split())

for index, j in enumerate(lists):
    score = int(int(j[1])) * 2 + int(int(j[2])) * 3 + int(j[3])
    scores[j[0]]= score

highest = max(scores, key=scores.get)
scores.pop(highest)
second_highest = max(scores, key=scores.get)

print(highest)
print(second_highest)