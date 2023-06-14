def count_integer_right_triangles(p):
    count = 0

    for a in range(1, p // 3 + 1):
        for b in range(a, (p - a) // 2 + 1):
            c = p - a - b
            if a * a + b * b == c * c:
                count += 1

    return count

#he code counts the number of integer right triangles that can be formed for a given perimeter p by iterating over the possible side lengths a and b and checking if the remaining side length c satisfies the Pythagorean theorem. 
# The count is then returned as the result.


def find_max_solutions():
    max_solutions = 0
    max_p = 0

    for p in range(1, 1001):
        solutions = count_integer_right_triangles(p)
        if solutions > max_solutions:
            max_solutions = solutions
            max_p = p

    return max_p


max_perimeter = find_max_solutions()
print(max_perimeter)

 
