# Decompress: COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf #2


L = int(input())
messages = []

for i in range(L):
    x = input().split()
    x[0] = int(x[0])
    messages.append(x)


for item in messages:
    print(item[1] * item[0])

