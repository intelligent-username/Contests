def initial_check(string, char1, char2):
    for i in range(0, len(string), 2):
        if string[i] != char1:
            return False
    
    for j in range(1, len(string), 2):
        if string[j] != char2:
            return False

    return True

def easy_heavy(T, N, strings):
    results = []

    for s in strings:
        char1 = s[0]
        char2 = s[1]

        if initial_check(s, char1, char2):
            if (s.count(char1) > 1 and s.count(char2) < 2) or (s.count(char2) > 1 and s.count(char1) < 2):
                results.append("T")
            else:
                results.append("F")
        else:
            results.append("F")

    return results

# Input
T, N = list(map(int, input().split()))
inputs = []

# Collect input strings
for _ in range(T):
    inputs.append(input())

# Output
outputs = easy_heavy(T, N, inputs)
for result in outputs:
    print(result)
