def is_prime(n):
    # Check if a number is prime
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_consecutive_primes(a, b):
    # Count the number of consecutive primes generated by the formula n^2 + a*n + b
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n

def find_coefficients():
    max_count = 0
    product = 0

    # Loop through all possible values of a and b within the given range
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            count = count_consecutive_primes(a, b)
            
            # Update the maximum count and product if a new record is found
            if count > max_count: #A TRACKER FOR SEEING
                max_count = count
                product = a * b
    
    return product

# Call the function to find the product of the coefficients a and b
result = find_coefficients()
print(result)
