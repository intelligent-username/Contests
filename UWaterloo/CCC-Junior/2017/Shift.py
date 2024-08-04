# SHIFTY SUM: COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf #2

N = int(input())
k = int(input())
sum = N

for x in range(1, k+1):
    N = N * 10
    sum += N

print(sum)