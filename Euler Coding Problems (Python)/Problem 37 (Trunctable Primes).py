def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    # Check if n is a truncatable prime number
    num_str = str(n)
    
    # Check left-to-right truncation
    for i in range(1, len(num_str)):
        if not is_prime(int(num_str[i:])): # Check if n is a left-truncatable prime
            return False
    
    # Check right-to-left truncation
    for i in range(1, len(num_str)):
        if not is_prime(int(num_str[:-i])): #Same logic as above but reversed 
            return False
    
    return True


#slice snytax [:4] means it gets everything from index 0 to 4 (4 is not incldued)
#[2:] means that it gets everything from index 2 until the end 

#Left-Truncatable Prime Check: 3797

#Iteration 1: n_str[1:] = "797". It checks if 797 is a prime number.
#Iteration 2: n_str[2:] = "97". It checks if 97 is a prime number.
#Iteration 3: n_str[3:] = "7". It checks if 7 is a prime number.
#All the substrings ("797", "97", and "7") are prime numbers, so the left-truncatable prime check passes.

#Right-Truncatable Prime Check: 3797

#Iteration 1: n_str[:3] = "379". It checks if 379 is a prime number.
#Iteration 2: n_str[:2] = "37". It checks if 37 is a prime number.
#Iteration 3: n_str[:1] = "3". It checks if 3 is a prime number.
#All the substrings ("379", "37", and "3") are prime numbers, so the right-truncatable prime check also passes.
#Since the number 3797 passes both checks, it is considered a truncatable prime so it returns true, which is super superrr important for our next string


def find_truncatable_primes():
    truncatable_primes = []
    num = 11  # Starting from 11 as single-digit primes are not considered truncatable, in daaa spec (READ)
    
    while len(truncatable_primes) < 11:
        if is_prime(num) and is_truncatable_prime(num): #checks if it is a prime, and a prime number from left to right when every digit is removed from each direction from left and right
            truncatable_primes.append(num) #appened the number that meets both conditions to the trunc primes list
        num += 1
    
    return truncatable_primes

truncatable_primes = find_truncatable_primes() #, this line of code calculates the list of truncatable primes by calling the find_truncatable_primes() function and 
#stores the result in the truncatable_primes
sum_of_truncatable_primes = sum(truncatable_primes)

print(sum_of_truncatable_primes)
