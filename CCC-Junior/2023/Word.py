# WORD HUNT IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2023/ccc/juniorEF.pdf #5

# String of Uppercase letters (TARGET WORD)
W = input()

# Number of rows in the grid
R = int(input())

# Number of columns in the grid
C = int(input())
grid = []

for _ in range(R):
    grid.append(input().split())


