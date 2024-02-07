# Party Inivitation: In Progress
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2014/stage%201/seniorEn.pdf #1


k = int(input())
m = int(input())

friends = list(range(1, k + 1))
print(friends)

for j in range(m):
    multiples = int(input())
    temp = 1
    while True:
        try:
            friends[(multiples * temp) - 1] = False
            temp += 1
        except:
            break
    for x in friends:
        if not x: #if x i false
            friends.pop(x)

for r in friends:
    print(r)


# for j in range(m):
#     multiples = int(input())
#     temp = 1
#     while multiples * temp <= k:
#         friends[multiples * temp - 1] = 0
#         temp += 1

# friends = [friend for friend in friends if friend != 0]

# for r in friends:
#     print(r)

