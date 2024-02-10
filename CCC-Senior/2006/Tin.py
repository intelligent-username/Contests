# Tin Can Telephone: In Progress
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2006/stage1/seniorEn.pdf #3

temp = list(map(int,input().split()))

Romy = (temp[0], temp[1])
Jules = (temp[2], temp[3])
violations = 0

N = int(input()) # Number of windows

# I will assume the buildings won't be bigger than the distance between Rom and Jul
for _ in range(N):
    # Each input is: number of corners the building has
    # Followed by the coordinates of the inputs.
    # All on one line, ofc

    temp = list(map(int, input().split()))
    
    corner_count = temp[0]
    for j in range(0, corner_count - 2, 2):
        x1 = x1
        y1 = y1
        x2 = x2
        y2 = y2
        # x1 is the first x-coordinate. x2 is the second x-coordinate
        if ((x1 >= Romy[0] and x1 <= Jules[0]) or (x1 >= Jules[0] and x1 <= Romy[0])) and (x2 >= Romy[0] and x2 <= Jules[0]) or (x2 >= Jules[0] and x2 <= Romy[0]):
            # If the x-coordinates are between/on the house(s)
            if y2 >= Romy[1] and y2 <= Jules[1] or y2 >= Jules[1] and y2 <= Romy[1]:
                # AND the y-coordinates are between/on the house(s)
                violations += 1

print(violations)