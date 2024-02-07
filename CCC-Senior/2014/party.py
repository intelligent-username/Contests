# Party Inivitation: In Progress
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2014/stage%201/seniorEn.pdf #1

k = int(input()) # Number of friends
m = int(input()) # 'm' rounds of removals

friends = list(range(1, k + 1))
print("The list is rn:", friends)

for j in range(m):
    multiples = int(input()) # Remove multiples of this number
    temp = 1
    while temp * multiples <= len(friends):
        friends[(multiples * temp) - 1] = False
        temp += 1

    print("Iteration", j, "of the list:", friends)

    for x in friends:
        if not x: #if x is false
            friends.remove(x)
    print("List after removal:", friends)

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

