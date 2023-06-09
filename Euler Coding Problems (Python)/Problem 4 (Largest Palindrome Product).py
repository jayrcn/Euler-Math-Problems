#just to note here Palindromic Number is a number that is read the same forwards and backwards such as 1221, 12321, 1111, 4774, etc (Largest product from a 2 digit palindromic is 9009 (91*99))
#for this prob we will try to find the same thing but for 3 DIGIT Numbers (ay talaga haha, 어렵지만 ㄱㅊ ㄱㅊ)

num = 1221
if str(num) == str(num)[::-1]:
    print("This is a palindromic number")
else:
    print("It aint a plaindromic number ")
