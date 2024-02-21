# Heavy-Light Composition

def initial_check(list):
    char1 = list[0]
    char2 = list[1]
    length = len(list)
    for j in range(0, length, 2):
        try:
            if list[j] != char1 and list[j+1] != char2:
                return False
        except:
            pass
    
    return True

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
    if initial_check(string):
        print("The letters are alternating")
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
        