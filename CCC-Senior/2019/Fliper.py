# Flipper: COMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/seniorEF.pdf #1

# H = Horizontal Flip
# V = Vertical Flip
original = [1, 2, 3, 4]

flips = input()
H = flips.count('H') % 2
V = flips.count('V') % 2


if H:
    original[0], original[1] = original[1], original[0]
    original[2], original[3] = original[3], original[2]
if V:
    original[0], original[2] = original[2], original[0]
    original[1], original[3] = original[3], original[1]

print(f"{original[0]} {original[1]}\n{original[2]} {original[3]}")

