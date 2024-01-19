# INCOMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2010/stage1/seniorEn.pdf 2010

# 2*R  + 3*S + D

n = int(input(""))

lists = [[] for _ in range(n)]
scores = []

for x in range(n):
    lists[x].append(input("").split())

for index, j in enumerate(lists):
    score = int(j[1]) * 2 + int(j[2]) * 3 + int(j[3])
    scores.append({'name': j[0], 'score': score})

for a, b in enumerate(scores):
    print(f"Input {a+1}: {b}")
# ????????????//