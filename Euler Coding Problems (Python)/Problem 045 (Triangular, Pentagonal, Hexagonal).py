def is_pentagonal(num):
    n = (1 + (1 + 24 * num) ** 0.5) / 6 #The is_pentagonal(num) function checks whether a given number num is a pentagonal number. It uses the formula (1 + (1 + 24 * num) ** 0.5) / 6 to calculate the pentagonal root of num. 
    #If the calculated value is an integer (i.e., the decimal part is zero), the function returns True; otherwise, it returns False.
    
    return n == int(n) #n == int(n): This checks if n is equal to its integer representation. If the decimal part of n is zero, then n is an integer, which means num is a hexagonal number. 
 #The function returns True in this case; otherwise, it returns False.

def is_hexagonal(num):
    n = (1 + (1 + 8 * num) ** 0.5) / 4 #Same logic as above
    return n == int(n)

def find_next_triangle():
    n = 286
    while True:
        triangle = n * (n + 1) // 2
        if is_pentagonal(triangle) and is_hexagonal(triangle): #If True then it returns the value of triangle (meaning that the value of triangle for both the functions equal the same) 
            #If false it keeps calling the pent and hexa function until they all meet at a number that is the same after calling the value of triangle on the respective functions
            return triangle
        n += 1

next_triangle = find_next_triangle()
print(next_triangle)

