# COLD COMPRESS - COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf #3

N = int(input())
inputs = []
str = ""

for i in range(N):
    inputs.append(input())

for x in inputs:
    temp = 1
    for s in range(len(x)):
        try:
            if x[s] == x[s+1]:
                temp += 1
            else: 
                str += f"{temp} {x[s]} "
                temp = 1
        except:
            str += f"{temp} {x[s]}"
            temp = 1
    str += "\n"

print(str)
