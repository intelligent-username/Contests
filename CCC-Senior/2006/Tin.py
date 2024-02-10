# Tin Can Telephone: In Progress
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2006/stage1/seniorEn.pdf #3

temp = list(map(int,input().split()))

Romy = (temp[0], temp[1])
Jules = (temp[2], temp[3])
violations = 0

N = int(input()) # Number of windows

for _ in range(N):
    # Each input is: number of corners the building has
    # Followed by the coordinates of the inputs.
    # All on one line, ofc

    temp = list(map(int, input().split()))

    corner_count = temp[0]
