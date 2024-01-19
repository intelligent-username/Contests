# Art: COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2020/ccc/juniorEF.pdf #3

N = int(input())
X = []
Y = []

for i in range(N):
    x, y = map(int, input().split(","))
    X.append(x)
    Y.append(y)

bottom_left = str(min(X) - 1) + "," + str(min(Y) - 1)
top_right = str(max(X) + 1) + "," + str(max(Y) + 1)
print(bottom_left)
print(top_right)