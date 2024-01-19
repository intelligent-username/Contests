# Are We There Yet: COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf
positions = [0]
temp = 0
output = ""


input_string = input()
substring_list = input_string.split(" ")

distances = [int(substring) for substring in substring_list]
print(distances)

for x in distances:
  temp += x
  positions.append(temp)
  
for j in positions:
  for r in positions:
    output += f"{str(abs(j - r))} "

  output = output[:-1]
  output += "\n"

print(output)
