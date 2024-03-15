# Occupied Parking: COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf #2

N = int(input())

day1 = input()
day2 = input()
counter = 0

for x in range(N):
    if day1[x] == day2[x] and day1[x] == "C":
        counter += 1

print(counter)

