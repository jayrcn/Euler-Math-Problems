def is_abundant(n):
    return sum(i for i in range(1, int(n/2) + 1) if n % i == 0) > n #If the sum is greater than n, it means n is an abundant number.
#If the sum is not greater than n, it means n is not an abundant number.

def sum_of_non_abundant_numbers(limit):
   
    abundant_numbers = [num for num in range(1, limit) if is_abundant(num)] #this line generates a list of all the abundant numbers within the specified limit. If the number is abundant
    abundant_sums = set(x + y for x in abundant_numbers for y in abundant_numbers)  #, this line calculates and stores all possible sums of pairs of abundant numbers in a set called abundant_sums. It takes each pair combination of 
    #numbers from the abundant_numbers list, calculates their sum, and adds it to the set. set() function is used to to eliminate duplicate values
    
    return sum(num for num in range(1, limit) if num not in abundant_sums) #In simpler terms, the line goes through a list of numbers from 1 to a certain limit. 
  #It checks each number to see if it is not in the set of abundant sums. 
  # If a number is not present in the set, it adds that number to a new list.

limit = 28124
result = sum_of_non_abundant_numbers(limit)
print(result)
