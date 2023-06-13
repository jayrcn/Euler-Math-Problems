def calculate_digital_sum(number):
    """
    Calculate the sum of the digits of a given number.
    """
    return sum(int(digit) for digit in str(number))


max_digital_sum = max(calculate_digital_sum(a ** b) for a in range(1, 100) for b in range(1, 100))


"""Another way to write it is:
# max_digital_sum = 0

    for a in range(1, 100):
        for b in range(1, 100):
            power = a ** b
            digit_sum = calculate_digital_sum(power)
            if digit_sum > max_digital_sum:
                max_digital_sum = digit_sum  #we can also use a max function here

    return max_digital_sum """

print(max_digital_sum)
