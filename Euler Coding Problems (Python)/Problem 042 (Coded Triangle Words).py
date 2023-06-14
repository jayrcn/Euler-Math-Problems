import string

# Read the input file and extract the words
with open("0042_words.txt") as file:
    words_data = file.read()
    words = words_data.replace('"', "").split(",")

def calculate_word_value(word):
    # Calculate the word value by summing the values of its characters
    value = 0
    for char in word:
        value += ord(char) - ord('A') + 1
    return value

def is_triangle_number(n):
    # Check if a number is a triangle number
    # A number is triangle if it satisfies the equation: n = k * (k + 1) / 2 for some positive integer k
    # We can rearrange the equation as: k^2 + k - 2n = 0 and solve for k using quadratic formula
    # If k is an integer, then n is a triangle number
    # Check if the discriminant is a perfect square to determine if k is an integer
    discriminant = 1 + 8 * n
    sqrt_discriminant = int(discriminant ** 0.5)
    return sqrt_discriminant * sqrt_discriminant == discriminant and (-1 + sqrt_discriminant) % 2 == 0 #I got math help with this fucntion the internet helps

def count_triangle_words(words):
    # Count the number of triangle words in the given list of words
    count = 0
    for word in words:
        word_value = calculate_word_value(word)
        if is_triangle_number(word_value):
            count += 1
    return count



# Count the number of triangle words
triangle_word_count = count_triangle_words(words)
print(triangle_word_count)
