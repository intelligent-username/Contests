# JERSEYS; INCOMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2015/stage%201/seniorEn.pdf #2


def main():
    J = int(input("# of jerseys: "))
    A = int(input("# of athletes: "))

    print("Getting size of jerseys")

    jerseys = []
    requested = []

    for j in range(J):
        jerseys.append(input(f"Jersey #{j}'s size: "))
    
    for a in range(A):
        # simpler version
        input = input(f"Input request {a}: ")
        requested.append(tuple(input.split()))
    

if __name__ == "__main__":
    main()