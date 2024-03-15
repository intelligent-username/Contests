# Rule of 3: INCOMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf #5

rule1 = input().split()
rule2 = input().split()
rule3 = input().split()

S, I, F = input().split()

# S is the number of Steps that must be  used, 
# I is the initial sequence, and 
# F is the final sequence

R, P, W = I, "", ""

for r in range(S):
    # Need to print 3 space-separated values: R, P, and W. 
    # R: Substitution rule number (1, 2 or 3)
    # P: Starting position of index where rule is used (indices start at 1)
    # W: Sequence that results from this substitution.
    # Then W needs to become the new R for the next iteration
    print(R, P, W)
    R = W
