# JERSEYS; COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2015/stage%201/seniorEn.pdf #2
# Not following specific request input template (in terms of output in the terminal),
# But this can be fixed by simply getting rid of quotation marks in input


J = int(input("# of jerseys: "))
A = int(input("# of athletes: "))

jerseys = {}
requested = {}
fulfillable = 0
taken_numbers = []

for j in range(J):
    size = input(f"(In Inventory) Jersey #{j+1}'s size: ")
    if size in jerseys:
        jerseys[size] += 1
    else: 
        jerseys[size] = 1


for a in range(A):
    request = input(f"Input request #{a+1}: ")
    if request in requested:
        requested[request] += 1
    else:
        requested[request] = 1

print("Testing ")
print("\nHAVES")
for q, r in jerseys.items():
    print("Size:", q, "      Count:", r)
print("\nNEEDS")
for x, y in requested.items():
    print("Request:", x, "   Count:", y)


for x,y in requested.items():
    if x[0] in jerseys and x[2] not in taken_numbers:
        fulfillable += 1
        taken_numbers.append(x[2])
        jerseys[x[0]] -= 1

print(fulfillable)
