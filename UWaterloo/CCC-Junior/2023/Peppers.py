# Peppers: COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2023/ccc/juniorEF.pdf #2

N = int(input("Number of: "))

values = {"Poblano": 1500, "Mirasol": 6000, "Serrano": 15500, "Cayenne": 40000, "Cayenne": 40000, "Thai": 75000, "Habanero": 125000}

score = 0

for i in range(N):
  pepper = input("Pepper: ")
  score += values[pepper]

print(score)
