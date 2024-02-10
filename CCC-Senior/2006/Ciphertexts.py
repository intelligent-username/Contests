# Attack of the Ciphertexts; IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2006/stage1/seniorEn.pdf #1 

pt1 = input()
ct1 = input()
pt2 = ""
ct2 = input()

# Use plaintext1 and cyphertext one to map letters to each other. 
# Then use the mapping of the letters to form plaintext2
# And then print plaintext2

keys = {}

for r in range(len(p1)):
    
    keys[pt1[r]]= ct1[r]
    keys[ct1[r]]= pt1[r]
