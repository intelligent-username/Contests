# Triangle: The Data Structure; IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/seniorEF.pdf # 5

N, K = list(map(int, input().split()))
# N is the number of rows
# K is the size of triangle to check
triangle = []
max_sum = 0
for _ in range(N):
    triangle.append(list(map(int, input().split())))
    # How is the sum calculated!? Unclear
