def get_sum_sq(n):
    number = 2 ** n
    sum = 0
    for a in str(number):
        sum = int(a) + sum
        
    return sum


print((get_sum_sq(1000)))
