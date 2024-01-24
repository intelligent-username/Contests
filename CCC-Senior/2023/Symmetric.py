# Symmetric Mountains; IN PROGRESS
#https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2023/ccc/seniorEF.pdf #2
# Gitdoc test test

# We will measure the asymmetric value of a crop as the sum of the absolute difference for
# Every pair of mountains equidistant from the midpoint of the crop
# Pair up the mountains from the outside working toward the centre 
# Find the asymmetric value for the most symmetric crop

N = int(input())
# # Of mountains

heights = list(map(int, input().split()))

print(heights)
