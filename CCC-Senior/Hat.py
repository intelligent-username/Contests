# Hat Circle

N = int(input()) # Even positive integer

people = []
count = 0

for _ in range(N):
    people.append(input())

half_length = len(people) // 2
first_half = people[:half_length]
second_half = people[half_length:]

for j in range(half_length):
    if first_half[j] == second_half[j]:
        count += 2

print(count)