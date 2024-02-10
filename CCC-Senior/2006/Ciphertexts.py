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
    one = pt1[r]
    two = ct1[r]
    if one not in keys:
        keys[one] = two
        keys[two] = one



# For testing delete later
# temp = 0
# for a,b in keys.items():

#     print(f"Key {a}, item {b}    |    ", end = "")
#     if temp == 4:
#         temp = 0
#         print()

for x in ct2:
    try:
        pt2 += keys[x]
    except:
        pt2 += "."

print(pt2)
