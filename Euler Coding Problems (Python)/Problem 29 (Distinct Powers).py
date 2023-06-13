terms = []

for a in range (2,101):
    for b in range (2,101):
        number = a ** b
        if not (number in terms): #removes repeats 
            terms.append(number)
print(len(terms))
    