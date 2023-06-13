def calculate_probability():
    peter_outcomes = [0] * 37  # There are 9 four-sided dice, so the maximum total is 9 * 4 = 36
    colin_outcomes = [0] * 37  # There are 6 six-sided dice, so the maximum total is 6 * 6 = 36

    # Calculate the number of outcomes for each total for Peter and Colin
    for p1 in range(1, 5):
        for p2 in range(1, 5):
            for p3 in range(1, 5):
                for p4 in range(1, 5):
                    for p5 in range(1, 5):
                        for p6 in range(1, 5):
                            for p7 in range(1, 5):
                                for p8 in range(1, 5):
                                    for p9 in range(1, 5):
                                        total = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
                                        peter_outcomes[total] += 1

    for c1 in range(1, 7):
        for c2 in range(1, 7):
            for c3 in range(1, 7):
                for c4 in range(1, 7):
                    for c5 in range(1, 7):
                        for c6 in range(1, 7):
                            total = c1 + c2 + c3 + c4 + c5 + c6
                            colin_outcomes[total] += 1

    # Calculate the total number of outcomes for Peter and Colin
    peter_total_outcomes = sum(peter_outcomes)
    colin_total_outcomes = sum(colin_outcomes)

    # Calculate the number of outcomes where Peter's total is greater than Colin's total
    peter_wins = 0
    for p in range(37):
        peter_wins += sum(peter_outcomes[p+1:]) * colin_outcomes[p] #For each sum p, this line calculates the number of times Peter wins. It sums the values in the peter_outcomes list starting from index p+1 to the end, and multiplies that sum 
        #by the corresponding value in the colin_outcomes list at index p. This calculation represents the number of wins for Peter for the current sum p, and it is added to the peter_wins variable.

    # Calculate the probability
    probability = peter_wins / (peter_total_outcomes * colin_total_outcomes)

    return round(probability, 7)


probability = calculate_probability()
print(probability)
