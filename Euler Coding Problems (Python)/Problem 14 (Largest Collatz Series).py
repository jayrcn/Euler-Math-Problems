cache = [0] * 1000000 #cache is used to see what numbers have been seen 

def collatz(n):
    if n == 1:
        return 1
    
    if n < 1000000 and cache[n] != 0: #for example col(10) >> 1 + col(5), col(5) we have seen is 6 so since it is the next term after col(10) we just do col(10) + 6 terms which equals 7 terms for col(10)
        return cache[n]
    
    if n % 2 == 0:
        return 1 + collatz(n//2) #these are basic collatz logic for if statements
    else:
        return 1 + collatz(3*n+1)
    
largest = 0 #length of collatz sequence of a number
start = 0 #keep track of the number

for i in range(1, 1000000):
    cache[i] = collatz(i) #how we setup the cache, everytime we increment by 1 we keep track of it in our cache
    if cache[i] > largest: #if cache is greater than largest 
        largest = cache[i] #then we found the largest sequence and keep track of it in the largest variable
        start = i #anytime we reset largest we also reset start 
    
print(start)


#col(5) >> 1 + col(16)  >> 2 + col (8) >> 3 + col(4) >> 4 + col(2) >> 5 + col(1) whetaln we hit col(1) that is the final term of the collatz series for the original number: 6 terms total
    
    