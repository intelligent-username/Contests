k = int(input())
m = int(input())

friends = [_ for _ in range(k)]

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
        if x == False:
            friends.pop(x)

for r in friends:
    print(r)

# k = int(input())
# m = int(input())

# friends = list(range(1, k + 1))

# for j in range(m):
#     multiples = int(input())
#     temp = 1
#     while multiples * temp <= k:
#         friends[multiples * temp - 1] = 0
#         temp += 1

# friends = [friend for friend in friends if friend != 0]

# for r in friends:
#     print(r)

