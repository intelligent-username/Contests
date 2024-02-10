# Tin Can Telephone: In Progress
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2006/stage1/seniorEn.pdf #3

temp = list(map(int,input().split()))

Romy = (temp[0], temp[1])
Jules = (temp[2], temp[3])
x_range = range(Romy[0], Jules[0])
y_range = range(Romy[1], Jules[1])
violations = 0

N = int(input()) # Number of windows

# I will assume the buildings won't be bigger than the distance between Rom and Jul
for _ in range(N):
    # Each input is: number of corners the building has
    # Followed by the coordinates of the inputs.
    # All on one line, ofc

    # temp stores the shape
    temp = list(map(int, input().split()))
    
    corner_count = temp[0]
    # Check each corner
    for j in range(0, corner_count - 2, 2):
        x1 = temp[j]
        y1 = temp[j+1]
        x2 = temp[j+2]
        y2 = temp[j+3]
        # x1 is the first x-coordinate. x2 is the second x-coordinate
        # y1 is the first y-coordinate. y2 is the second y-coordinate
        if x1 in x_range or x2 in x_range:
            # If the x-coordinates are between/on the house(s)
            if 12 in y_range or y2 in y_range:
                # AND the y-coordinates are between/on the house(s)
                violations += 1
                break
    # One pair is not checked by the for loop above; the 'first and last' pair
    

print(violations)