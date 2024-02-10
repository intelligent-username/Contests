# Attack of the Ciphertexts; IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2006/stage1/seniorEn.pdf #2

pt1 = input()
ct1 = input()
pt2 = ""
ct2 = input()

# Use plaintext1 and cyphertext one to map letters to each other. 
# Then use the mapping of the letters to form plaintext2
# And then print plaintext2

keys = {}

for r in range(len(pt1)):
    
    keys[pt1[r]]= ct1[r]
    keys[ct1[r]]= pt1[r]

print("The keys are", keys)

for x in ct2:
    try:
        pt2 += keys[x]
    except:
        pt2 += "."

print(pt2)
