# Fergunson Ball: COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2022/ccc/juniorEF.pdf #2

# -3 for foul
# +5 for score
# Points > fouls
# Determine # of players who have a star rating greater than 40
# Gold: more than 40 points all players

N = int(input("Number of players"))
counter = 0

for i in range(N):
  Points = int(input("Points: "))
  Fouls = int(input("Fouls: "))

  if Points * 5 - Fouls * 3 > 40:
    counter += 1

output = str(counter)

if counter == N:
  output += "+"

print(output)