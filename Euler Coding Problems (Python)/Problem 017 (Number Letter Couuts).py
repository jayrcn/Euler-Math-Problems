def number_to_words(n):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n == 1000:
        return "one thousand"
    elif n >= 100:
        hundreds = units[n // 100] + " hundred" #For examples (854), 854//100 = 8 (and it goes to the 8th index of the list which is the word "eight and adds the word "hundred at the end")
        if n % 100 == 0: 
            return hundreds
        else:
            return hundreds + " and " + number_to_words(n % 100) #if there is a reamainder and 854 does this so it returns 54
    
    elif n >= 20:
        return tens[n // 10] + " " + number_to_words(n % 10) #does 54//10 (the remiander from n % 100 is passed into here) (in which it goes into the 5th index of tens which is fifty and the does the remainder of 54)
    
    elif n >= 10: #remainder for the tens goes here (if it is lese then 10 it goes through these two test cases)
        return teens[n - 10]
    else:
        return units[n]

total_letters = sum(len(number_to_words(i).replace(" ", "")) for i in range(1, 1001)) #replaces the spaces with no spaces just to count letters straight w/o confusion of spaces
print(total_letters)
