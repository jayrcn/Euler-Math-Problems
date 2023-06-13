total = 0

for number in range(10, 1000000):
    digitSum = sum(int(digit) ** 5 for digit in str(number)) 
    if digitSum == number: ##if the sum of the (each digit) digits to the power of 5 equal to the original number we parsed through then add that to the total counter

         total += number

print(total)