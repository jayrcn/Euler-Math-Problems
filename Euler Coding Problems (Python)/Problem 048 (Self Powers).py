num = 0
for numbers in range(1,1001):
    num += numbers**numbers
print(str(num)[-10:])
