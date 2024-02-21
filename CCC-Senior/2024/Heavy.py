# Heavy-Light Composition

# A letter is heavy if it appears more than once
# Otherwise it's light

# Input
T, N = list(map(int, input().split()))
inputs = []
heavy = set()
light = set()

# Collect input strings
for _ in range(T):
    inputs.append(input().strip())

# Output
for string in inputs:
    alternating = True

    for i in range(1, N):
        if string[i] != string[i - 1]:
            alternating = False
            break
        elif string[i] not in light:
            light.add(string[i])
        else:
            heavy.add(string[i])
        
    print("T" if alternating else "F")
