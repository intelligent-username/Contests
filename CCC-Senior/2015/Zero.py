# BOSS SAYS; COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2015/stage%201/seniorEn.pdf (2015) #1

def main():
    k = int(input("# of #s to compute: "))
    # 100 000 >= K >= 0

    inputs = []

    for i in range(k):
        temp = int(input("Boss says: "))
        try:
            if temp > 0:
                inputs.append(temp)
            elif temp == 0:
                inputs.pop(0)
        except:
            raise Exception("Invalid input")
    # Won't follow input specification so the program is understandable by humans
    print("Profit:", sum(inputs))


if __name__ == "__main__":
    main()