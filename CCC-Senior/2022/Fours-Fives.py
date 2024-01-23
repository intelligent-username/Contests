# GOOD FOURS AND GOOD FIVES; INCOMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2022/ccc/seniorEF.pdf #1

N = int(input())

possibilities = 0
while N >= 0:
    if N % 5 == 0:
        possibilities += 1
    N -= 4

print(possibilities)