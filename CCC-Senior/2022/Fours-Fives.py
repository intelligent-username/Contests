# GOOD FOURS AND GOOD FIVES; INCOMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2022/ccc/seniorEF.pdf #1
# YET TO FINISH, BUG with 20 for example, 5, 4
# REDO, Streamline the whole thing?

def main():
    N = int(input("")) # Determine in how many ways this number can be formed by using 4s and 5s

    possibilities = 0

    # 20 has 2 ways
    # 40 has 3 ways
    # 60 has 4 ways
    # 80 has 5 ways

    if not ((N % 5) % 4): # Checks if it can be made with exclusively 4s and/or 5s

        if not (N % 5): # If value can be made with only 5s
            possibilities += 1

        if not (N % 4): # If value can be made with only 4s
            possibilities += 1
        
        if (N > 20): # If the value is greater than 20
            possibilities += (N - 20) // 20 # Find the number of 20s b/c each 20 can be made with 4s or 5s and therefore adds 1 possibility



        possible(possibilities)


    else:
        impossible()

def impossible():
    print("0")

def possible(p):
    print(f"{p}")

main()