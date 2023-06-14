def is_pentagonal(number):
    # Check if a number is pentagonal
    n = (1 + (1 + 24 * number) ** 0.5) / 6
    return int(n) == n

def find_min_pentagonal_difference():
    n = 1
    while True:
        pentagonal_n = n * (3 * n - 1) // 2

        m = n - 1
        while m > 0:
            pentagonal_m = m * (3 * m - 1) // 2
            difference = pentagonal_n - pentagonal_m

            if is_pentagonal(difference) and is_pentagonal(pentagonal_n + pentagonal_m):
                return difference

            m -= 1

        n += 1

# Call the function to find the minimum pentagonal difference
min_difference = find_min_pentagonal_difference()
print(min_difference)
