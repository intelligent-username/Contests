# FAVORITE TIMES; INCOMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf #4

# Start at Noon, find arithmetic series

# Steps
# Figure out how to encode time
# Figure out what the max increments of arithmetic series are (6? 4?)
# Then it's just simple math
Time = [12, 00]
Passed = int(input()) # The number of minutes passed
Hours = Passed // 60
Minutes = Passed - Hours * 60


