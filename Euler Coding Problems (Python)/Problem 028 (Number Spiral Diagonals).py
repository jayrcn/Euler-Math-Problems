def spiral_diagonal_sum(n):
    diagonal_sum = 1  # Start with the central number (1)
    current_number = 1  # Keep track of the current number
    step_size = 2  # The step size for each layer of the spiral
    count = 0  # Keep track of the number of steps

    for _ in range(1, n // 2 + 1):  # Iterate through each layer of the spiral
        for _ in range(4):  # Iterate through the four corners in each layer
            current_number += step_size  # Move to the next number
            diagonal_sum += current_number  # Add the current number to the diagonal sum #stackoverflow helped with this logic
            count += 1  # Increase the step count

        step_size += 2  # Increase the step size for the next layer

    return diagonal_sum


n = 1001  # We want to find the sum of the diagonal numbers up to the 1001 x 1001
sum = spiral_diagonal_sum(n)
print(sum)

