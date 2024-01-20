# GOOD FOURS AND GOOD FIVES; INCOMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2022/ccc/seniorEF.pdf #1

N = int(input())

possibilities = 0
# Find the number of ways to make a given number N by adding a combination of 4s and 5s or only 4s and 5s
# Four and Five have no factors in common
# LCM: 20
# 20 CAN BE MADE USING 5 4S OR 4 5S, no combinations
# So Each 20 is +2
# And everything else that that can be made is a factor of either 4 or 5 (Not both)

if not ((N % 5) % 4): # Checks if it can be made with exclusively 4s and/or 5s
    possibilities += 1
    twenties = N // 20 # Find number of twenties in the number
    N -= twenties * 20

    fives = N//5
    N -= 5 * fives

    fours = N // 4
    N -= 4 * fours

    possibilities += twenties * 2
    possibilities += fives
    possibilities += fours

    if N != 0:
        possibilities = 0

print(possibilities)