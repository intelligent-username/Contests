# Special Day: Complete
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2015/stage%201/juniorEn.pdf #1

# Check if before or after or on February 18

month = int(input())
day = int(input())

if month == 2 and day == 18:
    print("Special")
elif month > 2 or day > 18:
    print("After")
else:
    print("Before")