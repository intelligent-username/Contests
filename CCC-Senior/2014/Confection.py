# CONFECTION: IN PROGRESS
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2014/stage%201/seniorEn.pdf #3
def main():
    T = int(input()) # # of tests
    answers = []

    for _ in range(T):
        N = int(input()) # Number of cars
        cars = []
        for x in range(N):
            cars.append(int(input()))
            # The cars will be given from top to bottom
            # The cars will always use the numbers from 1 to N in order.
            # Need to figure out if I can put them in from 1 to 4
        
        answers.append(sliderchecker(cars, N))
    
    for x in answers:
        print(x)

# Will check if the cars can be stacked in 1,2,3....N order
def sliderchecker(cars, N):
    highest_rn = 0
    branch = []

    for q in range(N-1, -1, -1):  # Fix the range to include the first element
        if cars[q] == highest_rn + 1:
            highest_rn += 1
        elif branch and branch[-1] == highest_rn + 1: # "Branch and" ensures the branch is not empty
            highest_rn += 1
            branch.pop()
        else:
            branch.append(cars[q])

    if highest_rn == N and not branch:
        return "Y"
    
    while branch:
        if branch[-1] == highest_rn + 1:
            highest_rn += 1
            del branch[-1]
        else:
            return "N"

    return "Y"


if __name__ == "__main__":
    main()
