def find_digit_cancelling_fractions():
    fractions = []

    for numerator in range(10, 99):
        for denominator in range(11, 99):
            if numerator >= denominator:
                continue

            numerator_str = str(numerator)
            denominator_str = str(denominator)

            # Check if the numerator and denominator have a common digit
            for digit in numerator_str:
                if digit != '0' and digit in denominator_str:
                    # Cancel the common digit
                    simplified_numerator = int(numerator_str.replace(digit, '', 1)) #Lets say we have the fraction 49/98, it would cancel the 9s out and make the fraction 4/8 making it equal to 1/2
                    simplified_denominator = int(denominator_str.replace(digit, '', 1))

                    # Check if the simplified fraction is equal to the original fraction
                    if numerator * simplified_denominator == denominator * simplified_numerator:
                        fractions.append((numerator, denominator))

    product_numerators = 1
    product_denominators = 1

    # Calculate the product of the fractions
    for fraction in fractions:
        product_numerators *= fraction[0]
        product_denominators *= fraction[1]
        
        
    #For example, let's say we have a list of fractions [(2, 3), (4, 5), (6, 7)].

#Initially, product_numerators is set to 1, and product_denominators is set to 1.
#In the first iteration, the current fraction is (2, 3). So, product_numerators becomes 1 * 2 = 2, and product_denominators becomes 1 * 3 = 3.
#In the second iteration, the current fraction is (4, 5). So, product_numerators becomes 2 * 4 = 8, and product_denominators becomes 3 * 5 = 15.


    # Simplify the product fraction by dividing both numerator and denominator by their greatest common divisor
    gcd = greatest_common_divisor(product_numerators, product_denominators)
    product_numerators //= gcd
    product_denominators //= gcd

    return product_denominators

def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Call the function to find the product of the denominators
product = find_digit_cancelling_fractions()
print(product)
