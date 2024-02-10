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
    for j in range(0, corner_count - 2, 2):
        if ((temp[j] >= Romy[0] and temp[j] <= Jules[0]) or (temp[j] >= Jules[0] and temp[j] <= Romy[0])) and (temp[j+2] >= Romy[0] and temp[j+2] <= Jules[0]) or (temp[j+2] >= Jules[0] and temp[j+2] <= Romy[0]):
            # If the x-coordinates are between/on the house(s)
            if temp[j+1] >= Romy[1] and temp[j+1] <= Jules[1] or temp[j+1] >= Jules[1] and temp[j] <= Romy[1]:
                # AND the y-coordinates are between/on the house(s)
                violations += 1
