import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True #checks the condition whether or not it is a prime number

def check_conjecture():
    n = 9  # Starting from the first odd composite number
    while True:
        if not is_prime(n):
            found = False
            for i in range(1, int(math.sqrt(n//2)) + 1):
                if is_prime(n - 2 * i * i):
                    found = True
                    break
            if not found:
                return n
        n += 2  # Skipping even numbers

result = check_conjecture()
print(result)
