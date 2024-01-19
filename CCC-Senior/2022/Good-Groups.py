must_be = []
must_not_be = []
groups = []

X = int(input("Input X: ")) # Numbers of pairs that must be in the same group

for i in range(X):
    must_be.append(input(f"Must be same group input #{i+1}: "))

Y = int(input("Input Y: ")) # Number of pairs that must not be in the same group
for j in range(Y):
    must_not_be.append(input(f"Must not be together input #{j+1}: "))

G = int(input("Input G: ")) # Number of groups
for k in range(G):
    groups.append(input(f"Group #{k+1}: "))

print(
    f"Must be: {', '.join(must_be)}",
    f"Must not be: {', '.join(must_not_be)}",
    f"And fr: {' '.join(groups)}",
    sep='\n'
)

violations = 0
    
for group in range(G):
    for x in range(X):
        
        if must_be[x] in groups[group]:
            violations += 1
            break
    
    for y in range(Y):
    
        if must_not_be[y] in groups[group]:
            violations += 1
            break

print(violations)

