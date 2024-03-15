# Cold Caller; COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf

namber = ""

for x in range(4):
  namber += input()

if namber[1] == namber[2] and (namber[0] == '9' or namber[0] == '8') and (namber[3] == '8' or namber[3] == '9'):
  print("ignore")
else:
  print("answer")
