from math import factorial

total = 0
for number in range(10, 2540160): #digits 1-9 is not included for the logic of this problems so start at 10
    if number == sum(factorial(int(digit)) for digit in str(number)): #saying that if the number is equal to the sum of the factorial of each digit in the given number, 
        #the add that number to the total, then we keep doing it for all the numbers up to a given limit (I plugged and chugged for a random high number for the limit and when I kept increasing it it statyed stagant at 40730)
        total += number

print(total)
