answer = 0
for a in range(1, 1000): #for the range up to 1000
    if a % 3 == 0 or a % 5 == 0: #check if the number is a multiple of 3 or 5
        answer += a #if so add "a" to the THE ANSWER VARIABLE (answer = a + answer is also okay)
    print(answer) #PRINT ANSWER ONCE ALL INTERATIONS ARE DONE