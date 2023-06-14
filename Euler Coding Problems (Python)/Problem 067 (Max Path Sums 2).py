def read_triangle(file_path):
    # Read the triangle from a file and return it as a 2D list
    triangle = []
    with open(file_path, 'triangle.txt') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            triangle.append(row)
    return triangle


def maximum_path_sum(triangle):
    # Calculate the maximum path sum using dynamic programming
    
    # Start from the second last row and iterate upwards
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # Choose the maximum value from the two adjacent numbers below
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
    # The maximum sum will be at the top of the triangle
    return triangle[0][0]


# Test the function with the given triangle file
file_path = "triangle.txt"
triangle = read_triangle(file_path)
result = maximum_path_sum(triangle)
print("The maximum total from top to bottom is:", result)
