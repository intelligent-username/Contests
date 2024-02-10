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
    keys[one] = two
    keys[two] = one



# For testing delete later
# for a,b in keys.items():

#     print(f"{a} maps to {b}    |    ")

for x in ct2:
    print("X:", x, end = "")
    if x in keys:
        print(f"keys[x] is {keys[x]}")
        pt2 += keys[x]
    else:
        pt2 += "."

print(pt2)
