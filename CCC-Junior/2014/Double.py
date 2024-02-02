p1 = 100
p2 = 100

N = int(input())
rolls = []

for x in range(N):
    rolls += input().split()

for x in range(0, len(rolls), 2):
    print(x)
    if x[0] > x[1]:
        p2 -= x[0]
    elif x[1] > x[0]:
        p1 -= x[1]

print(p1)
print(p2)
