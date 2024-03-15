# Crazy Fencing: COMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2021/ccc/seniorEF.pdf #1

N = int(input())

heights = list(map(int ,input().split()))
# Heights of adjacent trapezoids

widths = list(map(int, input().split()))
base_temp = (heights[0] + heights[1]) / 2

areas = [0] * N

for x in range(N):
    base_temp = (heights[x] + heights[x+1]) / 2
    areas.append(base_temp * widths[x])

result = sum(areas)

if result.is_integer():
    result = int(result)

print(result)
