# Pretty Average Primes: INCOMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/seniorEF.pdf #2


# A number will be given, must find
# A combination of two primes
# Such that the average of these primes
# Is that number
# The given numbers will be greater than 4
def is_prime(num):
    for i in range(3, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_for_average(N):
    # Iterate from 2 to N/2 to find two primes whose average is N
    for A in range(2, N // 2 + 1):
        B = N - A
        if is_prime(A) and is_prime(B):
            return [A, B]
    
    return False

answers = ""

T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())  # Input N for each test case
    primes = find_primes_for_average(N)
    answers += f"{primes[0]} {primes[1]}"
    answers += "\n"

print(answers)


