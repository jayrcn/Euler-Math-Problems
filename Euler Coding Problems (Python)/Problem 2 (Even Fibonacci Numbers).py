first = 1
second = 2
evenfibnum = [second] #keep our fib numbers as a list type, and the first number in our fib sequence is 2 (which is assigned to our "second" variable)

while True:
    fibonacci = first + second #ex one sum in the sequence is (5+8=13, then when it loops again assuming all the if statements are true, then it would do 8+13 for the next iteration)
    first = second #equate first number as the second number (after 5 + 8 =13's iteration, 8 is assiigned as the first number in the second iteration making it 8 + fib number (13) = new fib number)
    second = fibonacci #make second number equal to the fib number (ex: in the iteration above, since it had an answer of 21, then 21 is the second number in the next iteration)

    if fibonacci > 4000000: #this ensures that the total sum of all the fib numbers does not go pass 4 million
        break
    
    if fibonacci % 2 == 0: #if even within the fib seqence, then it adds to the ANSWER list
        answer.append(fibonacci)
    
    
result = sum(evenfibnum) #this sums the list of EVEN numbers in the fib sequence whos values dont exceed 4 mil
print(result) #shows the tota(sum) amount of the numbers in the list

