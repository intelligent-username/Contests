# Modern Art; IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2021/ccc/seniorEF.pdf #2

# Number of rows
M = int(input())

# Number of columns
N = int(input())

# Artist's choices
K = int(input())

Canvas = [["B"] * N] * M
print("Canvas is", Canvas)

for x in range(K):
    request = input().split()
    direction = request[0]
    index = int(request[1])

    if direction == "R":
        # Then do row
        for x in range(N):
            if Canvas[index][x] == "B":
                Canvas[index][x] = "G"
            else:
                Canvas[index][x] = "B"

            print("Canvas is ", Canvas)

    else:
        # Else it's "C", do column
        for j in Canvas:
            # print("J is ", j)
            if j[index] == "B":
                j[index] = "G"
            else:
                j[index] = "B"
            print("Canvas is", Canvas)
            

print(Canvas)
answer = Canvas.count("G")
print(answer)
