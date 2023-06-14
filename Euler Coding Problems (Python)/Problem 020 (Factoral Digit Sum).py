import math
n = 100
answer = 0
print((math.factorial(n)))
for digit in str(math.factorial(n)):
    answer = answer + int(digit)
print(answer)


