# Read the names from the file
with open("0022_names.txt") as file:
    names = file.read().replace('"', '').split('','')


def calculate_name_score(name):
    # Calculate the score for a given name
    score = sum(ord(ch) - ord('A') + 1 for ch in name) #the ord() function returns the Unicode code for a character, this function make sure that A is 1 and B is 2 C is 3 etc
    #ex: Ord(C=67) - ord(A = 65) + 1 = 3, so 3 is equal to C
    return score

def total_name_scores(names):
    # Sort the names in alphabetical order
    names.sort()

    total_score = 0
    for i, name in enumerate(names, start=1): #enumerate function is to get back both the index adn value of each item in the sequence
        # Calculate the name score multiplied by its position in the list
        name_score = calculate_name_score(name)
        total_score += name_score * i #value of the name times its postion 

    return total_score


# Calculate the total name scores
result = total_name_scores(names)
print(result)
