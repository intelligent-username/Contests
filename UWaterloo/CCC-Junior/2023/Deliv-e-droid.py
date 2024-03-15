# Deliv-E-Droid COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2023/ccc/juniorEF.pdf #1

P = int(input()) # # Of Packages Delivered (+50)
C = int(input()) # # of Collisions (-10)

F = 50*P - 10*C #Final Score

if P > C:
    F += 500

print(F)
