def is_reversible(n):
    # Check if a number is reversible
    
    # Check for leading zeros
    if str(n)[0] == '0':
        return False
    
    # Reverse the number
    reversed_n = int(str(n)[::-1])
    
    # Check if the sum consists entirely of odd digits
    sum_digits = n + reversed_n
    for digit in str(sum_digits):
        if int(digit) % 2 == 0:
            return False
    
    return True


def count_reversible_numbers(limit):
    # Count the number of reversible numbers below the given limit
    
    count = 0
    
    # Iterate through the range of numbers
    for n in range(1, limit):
        if is_reversible(n):
            count += 1
    
    return count


# Test the function with the given limit
limit = 10 ** 9
result = count_reversible_numbers(limit)
print(result)
