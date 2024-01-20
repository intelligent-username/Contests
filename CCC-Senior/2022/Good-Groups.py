# GOOD GROUPS; INCOMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2022/ccc/seniorEF.pdf #2
# Again not following exact specific input accepting format in the terminal, can simply remove prompts inside of the quotations marks to do so. 

must_be = []
must_not_be = []
groups = []

X = int(input("# of Student Combinations that MUST be in the same group: ")) # Numbers of pairs that must be in the same group

for i in range(X):
    must_be.append(input(f"Must be same group input #{i+1}: "))

Y = int(input("# Of student Combinations that MUST NOT be in the same group: ")) # Number of pairs that must not be in the same group
for j in range(Y):
    must_not_be.append(input(f"Must not be together input #{j+1}: "))

G = int(input("Number of Groups MADE: ")) # Number of groups
for k in range(G):
    groups.append(input(f"Group #{k+1}: "))

violations = 0
    
for required in must_be:
    if required not in groups:
        violations += 1

for illegals in must_not_be:
    if illegals in groups:
        violations += 1    

print(violations)