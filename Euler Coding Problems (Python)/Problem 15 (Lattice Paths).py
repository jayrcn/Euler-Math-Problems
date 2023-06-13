import math
gridsize = 20 #grid size
def mathyfunction(n):
    return math.factorial(n) #20 factorial to get all posible combos for 20 ways 
def calculate(n,k):
    return(mathyfunction(n)/(mathyfunction(n-k)*mathyfunction(k)))
answer = calculate(gridsize*2, gridsize)
print(answer)
