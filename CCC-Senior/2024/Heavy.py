# Heavy-Light Composition

# A letter is heavy if it appears more than once
# Otherwise it's light

T, N = list(map(int,input().split()))

inputs = []
heavy = []

for x in range(T):
    inputs.append(input().split())

# Determine if they're alternating heavy letters
for r in inputs:
    for j in r:

