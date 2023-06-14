def has_repeated_digits(n):
    digits = set()
    for digit in str(n):
        if digit in digits:
            return True #checks if there is a repeated digit and there is, returns true and adds it to the set() (list in a way)
        digits.add(digit)
    return False

def is_pandigital(n):
    digits = set(str(n))
    return len(digits) == 9 and '0' not in digits

largest_pandigital = 0

for i in range(1, 100000):
    concatenated_product = ""
    for j in range(1, 10):
        concatenated_product += str(i * j)
        if len(concatenated_product) >= 9:
            break
    if is_pandigital(concatenated_product) and not has_repeated_digits(concatenated_product) and len(concatenated_product) >= 9: #for the repeated digit function we want it to return false to ensure that there is no digit that repeates itself 
        #(if it returned true that means it would allow repeating digits) #the length condtion just ensures we get a string of 9 without any repeating digits
        pandigital_num = int(concatenated_product)
        if pandigital_num > largest_pandigital:
            largest_pandigital = pandigital_num

print(largest_pandigital)


#it is possible to use a max function somewhere maybe??
