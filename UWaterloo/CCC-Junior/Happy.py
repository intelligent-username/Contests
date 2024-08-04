# Happy or Sad: COMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2015/stage%201/juniorEn.pdf

inp = input()

happy = inp.count(":-)")
sad = inp.count(":-(")

if happy == 0 and sad == 0:
    print("none")
elif happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
else:
    print("unsure")