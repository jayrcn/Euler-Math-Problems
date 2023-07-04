from math import isqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def solve_problem(limit):
    primes = [2]  # List to store prime numbers
    max_len = 0  # Maximum length of consecutive primes
    result = 0  # Result to store the prime sum

    # Generate a list of primes up to the given limit
    for num in range(3, limit, 2):
        if is_prime(num):
            primes.append(num)

    # Iterate over different starting points and lengths
    for start in range(len(primes)):
        prime_sum = 0
        length = 0

        for i in range(start, len(primes)):
            prime_sum += primes[i]
            length += 1

            if prime_sum >= limit:
                break

            if length > max_len and is_prime(prime_sum):
                max_len = length
                result = prime_sum

    return result

limit = 10**6  # Set the limit to cover the prime range
result = solve_problem(limit)
print(result)
