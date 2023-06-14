def sum_of_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0) # in n = 12, i = 1,2,3,4,6 b/c they divide into 12 evenly w/ no remainder

def amicable_numbers(limit):
    amicable_sum = 0 #This variable will store the sum of all the amicable numbers found.
    for i in range(1, limit): 
        sum1 = sum_of_divisors(i) #Calculate the sum of its divisors using the sum_of_divisors() function and store it in the variable sum1.
        sum2 = sum_of_divisors(sum1) #Calculate the sum of divisors for sum1 and store it in the variable sum2.
        if i == sum2 and i != sum1: #Check if i is equal to sum2 and also different from sum1. 
            #If this condition is true, it means that i is an amicable number.
            
            # If the above condition is true, it means 'i' is an amicable number
        # Add 'i' to the amicable_sum variable
            amicable_sum += i
    return amicable_sum

limit = 10000
result = amicable_numbers(limit)
print(result)

#12 is not an amicable number
