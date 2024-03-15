# Exactly Electrical: COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf #3

start = list(map(int, input.split()))
end = list(map(int, input.split()))

x = abs(start[0] - end [0])
y = abs(start[1] - end [1])
distance = x + y

charge = int(input())

if charge < distance:
    print("N")
elif (charge - distance) % 2:
    print("Y")
else:
    print("N") 