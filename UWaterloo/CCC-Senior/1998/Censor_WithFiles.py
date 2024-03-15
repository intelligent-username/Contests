# CCC Before Senior/Junior Categories
# CENSOR: COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/1998/stage1/1998CCCStage1Contest.pdf #1

# Open input file for reading
with open("censor.in", "r") as file:
    N = int(file.readline())
    inputs = [file.readline().strip() for _ in range(N)]

# Process censoring
for i in range(N):
    words = inputs[i].split()
    for j in range(len(words)):
        if len(words[j]) == 4:
            words[j] = "****"
    inputs[i] = " ".join(words)

# Open output file for writing
with open("censor.out", "w") as file:
    # Write modified lines to the output file
    file.write("\n\n".join(inputs))
