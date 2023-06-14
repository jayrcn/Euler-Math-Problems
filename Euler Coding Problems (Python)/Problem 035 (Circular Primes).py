def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_rotations(n):
    rotations = []
    n_str = str(n)
    for i in range(len(n_str)):
        rotation = int(n_str[i:] + n_str[:i]) #we concatenate the strings of the partial digits of each number and combine it in order to "rotate the number" as the function intends to do 
        rotations.append(rotation)
    return rotations

def count_circular_primes():
    count = 0 #counter check to see how many circular primes there are when the conditions in the for statement are all met
    for num in range(2, 1000000):
        if is_prime(num):
            rotations = get_rotations(num) #if number is prime it will do the rotation of each prime number is parses through from 2 to 1 milly
            if all(is_prime(rot) for rot in rotations):
                count += 1
    return count

circular_primes_count = count_circular_primes()
print(circular_primes_count)
