from itertools import permutations

def has_property(num):
    primes = [2, 3, 5, 7, 11, 13, 17]
    digits = str(num)
    
    for i in range(1, 8):
        sub_num = int(digits[i:i+3])
        if sub_num % primes[i-1] != 0: #We then check if the extracted sub_num is divisible by the 
        #corresponding prime number at index i-1 in the primes list.
        #If the remainder of sub_num divided by primes[i-1] 
        # is not equal to zero (indicating that sub_num is not divisible by the prime number), we return False.
            return False
    
    return True

def solve_problem():
    pandigitals = permutations('0123456789')
    result = 0
    
    for pandigital in pandigitals:
        num = int(''.join(pandigital))
        if has_property(num):
            result += num
    
    return result

result = solve_problem()
print(result)
