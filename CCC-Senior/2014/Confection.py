# CONFECTION: IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2014/stage%201/seniorEn.pdf #3
def main():
    T = int(input()) # # of tests

    for _ in range(T):
        N = int(input()) # Number of cars
        cars = []
        for x in range(N):
            cars.append(int(input()))
            # The cars will be given from top to bottom
            # The cars will always use the numbers from 1 to N in order.
            # Need to figure out if I can put them in from 1 to 4
        
        print(sliderchecker(cars, N))

# This function will check if the cars can be stacked in 1,2,3....N order
def sliderchecker(cars, N):
    highest_rn = 0
    branch = []
    for q in range(N-1, 0, -1):
        if cars[q] == highest_rn + 1:
            highest_rn += 1
        elif branch[0] == highest_rn + 1:
            highest_rn += 1
            branch.pop()
        else:
            branch.append(cars[q])
            cars.remove(q)
    if not highest_rn and not branch:
        return "Y"
    print("Branch is", branch)
    while branch:
        if branch[0] == highest_rn + 1:
            highest_rn += 1
            branch.pop()
        else:
            return "N"
            
    return "Y"

if __name__ == "__main__":
    main()
