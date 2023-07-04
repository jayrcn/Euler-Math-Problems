from itertools import permutations
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

def find_largest_pandigital_prime():
    digits = "987654321"
    
    for length in range(len(digits), 0, -1):
        perms = permutations(digits[:length])
        
        for perm in perms:
            num = int("".join(perm))
            
            if is_prime(num):
                return num
    
    return None

largest_pandigital_prime = find_largest_pandigital_prime()
print(largest_pandigital_prime)
