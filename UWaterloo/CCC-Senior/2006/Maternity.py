# Maternity; DONE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2006/stage1/seniorEn.pdf #1

# Doing an easier question for a change

p1 = input()
p2 = input()

# Number of offspring to check
X = int(input())
offspring = []

for _ in range(X):
    offspring.append(input())

possibilities = []

for each in offspring:
    temp = True # Be optimistic and assume it is their child
    for char in each:
        if char.isupper():
            if char in p1 or char in p2:
                continue
            else:
                temp = False
        else:
            if char in p1 and char in p2:
                continue
            else: 
                temp = False

    possibilities.append(temp)
    

for x in possibilities:
    if x:
        print("Possible baby")
    else:
        print("Not their baby!")
