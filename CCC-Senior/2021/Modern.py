# Modern Art; COMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2021/ccc/seniorEF.pdf #2

# Number of rows
M = int(input())

# Number of columns
N = int(input())

# Artist's choices
K = int(input())

Canvas = [["B" for _ in range(N)] for _ in range(M)]
# print("Canvas is", Canvas)

for x in range(K):
    request = input().split()
    direction = request[0]
    index = int(request[1]) - 1

    if direction == "R":
        # Then do row
        for L in range(N):
            if Canvas[index][L] == "B":
                Canvas[index][L] = "G"
            else:
                Canvas[index][L] = "B"

    else:
        # Else it's "C", do column
        for j in Canvas:
            # print("J is ", j)
            if j[index] == "B":
                j[index] = "G"
            else:
                j[index] = "B"
            

# print(Canvas)
flat_canvas = [item for sublist in Canvas for item in sublist]
answer = flat_canvas.count("G")
print(answer)
