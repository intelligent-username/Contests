# Pretty Average Primes: INCOMPLETE
# https://cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/seniorEF.pdf #2


# A number will be given, must find
# A combination of two primes
# Such that the average of these primes
# Is that number
def main():
    T = int(input()) # Number of test cases
    requirements = []

    # Integers between 4 and 1 billion
    for _ in range(T):
        requirements.append(int(input()))



def prime_finder(num):
    # If the number is even (remember it's greater than 2)
    # Then not prime obviously
    if not num % 2:
        return False
    
    digit_sum = sum(int(digit) for digit in str(abs(num)))

    # If the sum of the digits is divisible by 3, return (not necessary? delete?)
    if digit_sum % 3:
        return False
    
    temp = 3
    while temp < num:
    # for j in range(3, num, 2), not checking even numbers obviously:
        if num // temp == 0: # if divisble OK
            return False
        temp += 2
    

if __name__ == "__main__":
    main()