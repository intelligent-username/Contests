# CENSOR: COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/1998/stage1/1998CCCStage1Contest.pdf #1

N = int(input())
inputs = []

for x in range(N):
    inputs.append(input())

for L in inputs:
    for x in L:
        if len(x) ==  4:
            L = ""
string = ""
for R in inputs:
    string += R
    string += "\n\n"
string = string[:-2]
print(string)


