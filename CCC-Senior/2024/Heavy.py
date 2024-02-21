# Heavy-Light Composition

# Check if alternating letters exist
def initial_check(list, char1, char2):
    
    length = len(list)
    truth1 = True
    truth2 = True


    for x in range(0, length, 2):
        if list[x] != char1:
            truth = False
    
    for r in range(1, length, 2):
        if list[r] != char2:
            truth2 = False

    if truth1 and truth2:
        return False
    elif truth1:
        truth1
    elif truth2:
        return truth2
    return False

# A letter is heavy if it appears more than once
# Otherwise it's light

# Input

 
T, N = list(map(int, input().split()))
inputs = []
outputs = []

# Collect input strings
for _ in range(T):
    inputs.append(input().strip())

# Output
for string in inputs:
    heavy = set()
    light = set()

    char1 = string[0]
    char2 = string[1]
    if initial_check(string, char1, char2):
        print("The letters are alternating")
        if (string.count(char1) > 1 and string.count(char2) < 2) or (string.count(char2) > 1 and string.count(char1) < 2):
            print("T")
        else:
            print("F")

    else:
        print("The letters aren't alternating")
        print("F")
    

    # for i in range(1, N):
    #     if string[i] != string[i+2] and string[i+1] != string[i+1]:
    #         otuputs.append(False)
    #         break
    #     if string[i] == string[i - 1]:
    #         outputs.append(False)
    #         break
    #     elif string[i] not in light:
    #         light.add(string[i])
        
    #     elif string[i] in heavy:
            
        
    #     else: # Final condition; it's in light, so must be added to heavy
    #         heavy.add(string[i])
        