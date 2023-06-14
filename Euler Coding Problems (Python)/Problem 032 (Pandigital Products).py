def is_pandigital(n, m, product):
    # Concatenate the numbers n, m, and product into a string
    # Sort the string and check if it is a pandigital number
    pandigital_str = str(n) + str(m) + str(product)
    sorted_str = sorted(pandigital_str)
    return ''.join(sorted_str) == '123456789'

def find_pandigital_products():
    products = set()  # Set to store unique pandigital products

    # Iterate through possible values of n, m, and product
    for n in range(1, 10000):
        for m in range(1, int(10000/n)+1): #+1 is there to ensure max value is calculated for range to be included in the iteration
            product = n * m

            # Check if the product is pandigital
            if is_pandigital(n, m, product):
                products.add(product)

    return sum(products)

# Find the sum of all pandigital products
sum_of_pandigital_products = find_pandigital_products()
print(sum_of_pandigital_products)

#Join():Join all items in a tuple into a string
#Sorted():  sorted function in Python by default arranges items in ascending order by deafualt usually 
