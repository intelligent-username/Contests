# GOOD GROUPS; COMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2022/ccc/seniorEF.pdf #2
# Again not following exact specific input accepting format in the terminal, can simply remove prompts inside of the quotations marks to do so. 

must_be = []
must_not_be = []
groups = []

X = int(input("# of Student Combinations that MUST be: ")) 

for i in range(X):
    must_be.append(set(input(f"Must be same group input #{i + 1}: ").split()))

Y = int(input("# Of student Combinations that MUST NOT be: ")) 

for j in range(Y):
    must_not_be.append(set(input(f"Must not be together input #{j + 1}: ").split()))

G = int(input("Number of Groups MADE: ")) 

for k in range(G):
    groups.append(set(input(f"Group #{k + 1}: ").split()))

violations = 0

for required in must_be:
    if not any(required.issubset(group) for group in groups):
        violations += 1

for illegals in must_not_be:
    if any(illegals.issubset(group) for group in groups):
        violations += 1

print("Violated", violations, "Times")
