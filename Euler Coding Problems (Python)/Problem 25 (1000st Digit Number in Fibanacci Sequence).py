prev = 0
current = 1
index = 1

while True:
    current = prev + current 
    prev = current - prev
    
    #ex: c: 0+1 = 1 so prev = 1-0 = 1,   
    # f2: c = 1+1 = 2, prev: 2-1 = 1, 
    # f3: c: 2+1 = 3, prev: 3-1 = 2.... ETC
    
    index += 1
    if (len(str(current)) >= 1000): #keep looping until a number with a length of 1000 digits is reached and print out its index counter
        break
print(index)