from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def solve_problem():
    primes = [i for i in range(1000, 10000) if is_prime(i)]
    
    for prime in primes:
        perms = set(permutations(str(prime)))
        
        for perm in perms:
            perm_num = int(''.join(perm))
            
            if perm_num > prime and perm_num in primes:
                diff = perm_num - prime
                next_num = perm_num + diff
                
                if next_num in primes and set(str(next_num)) == set(perm):
                    return str(prime) + str(perm_num) + str(next_num)
    
    return None

result = solve_problem()
print(result)
