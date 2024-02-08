# Maternity; IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2006/stage1/seniorEn.pdf #1

# Input genetic profiles of parents
p1 = input()
p2 = input()

# Number of offspring to check
X = int(input())
offspring = []

# Input attributes of each baby
for _ in range(X):
    offspring.append(input())

possibilities = []

# Check each baby
for each in offspring:
    temp = True  # Be optimistic and assume it is their child
    for i, char in enumerate(each):
        if char.isupper():
            # Check if the dominant allele is present in the corresponding position of either parent
            if char not in (p1[i].upper(), p2[i].upper()):
                temp = False
                break
        else:
            # Check if the recessive allele is present in the corresponding position of both parents
            if char not in (p1[i].lower(), p2[i].lower()):
                temp = False
                break

    possibilities.append(temp)

# Output results
for x in possibilities:
    if x:
        print("Possible baby")
    else:
        print("Not their baby!")
