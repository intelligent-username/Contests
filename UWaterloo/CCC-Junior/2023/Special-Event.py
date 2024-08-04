# Special Event: COMPLETE
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2023/ccc/juniorEF.pdf #3

# Number of people
N = int(input())

# Initialize availability lists for each day
days = [[0] * N for _ in range(5)]

# Populate availability lists based on user input
for x in range(N):
    availability = input()
    for day, status in enumerate(availability):
        if status == "Y":
            days[day][x] = 1

# Find the day(s) with the maximum attendance
max_attendance = max(sum(day) for day in days)

# Output: List of day numbers with maximum attendance
answer = [str(day + 1) for day, attendance in enumerate(days) if sum(attendance) == max_attendance]

# Print the result
print(",".join(answer))
