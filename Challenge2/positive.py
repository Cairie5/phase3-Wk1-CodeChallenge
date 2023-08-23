# Define a function named positive_count with three arguments: a, b, and c.
def positive_count(a, b, c):
    # Check if at least two out of the three numbers are positive
    return (a > 0 and b > 0) or (a > 0 and c > 0) or (b > 0 and c > 0)

# Call the positive_count function with arguments 10, 5, and 2.
result = positive_count(10, 5, 2)

# Print the result returned by the positive_count function.
print(result)
