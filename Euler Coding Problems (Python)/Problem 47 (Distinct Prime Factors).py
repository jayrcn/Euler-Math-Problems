def prime_factors_count(n):
    factors = set()
    i = 2

    while i * i <= n:
        if n % i == 0:
            factors.add(i)  
            n //= i # n = n//1 (ex 25//5 = 5) #if we have 25, 25 % 5 == 0 so it will be added to the set list of factors (the number 5)
        else:
            i += 1 #if n % i != 0 then it adds one to check the prime factors up to the square root of n (ex: 25 goes through i=2,3,4,5) #6 is not inculdued b/c 36 > 25 which doesnt satsify the conditon

    

    return len(factors) #checks for  prime factors (how many are in each number)

def find_consecutive_numbers(n):
    count = 0
    consecutive = 0
    num = 2

    while consecutive < n:
        if prime_factors_count(num) == n:
            count += 1
            if count == n:
                return num - n + 1
        else:
            count = 0

        num += 1

    return None

result = find_consecutive_numbers(4)  # Change the argument to the desired number of consecutive numbers

print(result)


#searches for the smallest number that has a specified number of consecutive prime factors. 
# It iterates over numbers, checks their prime factors count using the prime_factors_count function, 
# and returns the first number that meets the criteria.