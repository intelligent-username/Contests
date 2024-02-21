# Heavy-Light Composition

# A letter is heavy if it appears more than once
# Otherwise it's light

# Input
T, N = list(map(int, input().split()))
inputs = []

# Collect input strings
for _ in range(T):
    inputs.append(input().strip())

# Output
for string in inputs:
    alternating = True
    heavy = set()
    light = set()

    for i in range(1, N):
        if string[i] != string[i - 1]:
            alternating = False
            break
        elif string[i] not in light:
            light.add(string[i])
        else: # Final condition; it's in light, so must be added to heavy
            heavy.add(string[i])
        
    print("T" if alternating else "F")
