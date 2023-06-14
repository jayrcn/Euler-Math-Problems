def same_digit_multiple():
    # Find the smallest positive integer that can be multiplied by 1, 2, 3, 4, 5, and 6
    n = 1
    while True:
        # Convert the number and its multiples to strings #got logic from stackO
        number_str = str(n)
        multiples_str = [str(n * i) for i in range(2, 7)]
        
        #n is initialized to 1, as we start checking from the smallest positive integer.
        #Inside the while loop, the variable number_str is assigned the string representation of n.
        #The multiples_str list is created using a list comprehension. It contains the string representations of n multiplied by each number from 2 to 6.
        
        # Sort the digits in each number
        number_digits = sorted(number_str)
        multiples_digits = [sorted(num) for num in multiples_str]
        #he digits in number_str are sorted using the sorted() function and stored in the number_digits variable.
        #For each string in multiples_str, the digits are sorted using sorted() and a new list comprehension. 
        # The resulting sorted digit lists are stored in the multiples_digits list.
        
        # Check if all the multiples have the same set of digits as the number
        if all(digit_set == number_digits for digit_set in multiples_digits):
            return n
        
        n += 1 #n (which is the number we are currently checking increases by one if conditions aint met)


# Test the function
result = same_digit_multiple()
print(result)
