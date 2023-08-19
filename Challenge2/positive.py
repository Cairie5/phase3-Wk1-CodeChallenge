def positive_count(a=10, b=-5, c=2):
    # Calculate the sum of positive numbers among the given arguments
    positive_sum = sum(num for num in (a, b, c) if num > 0)
    
    # Check if the sum of positive numbers is greater than or equal to 2
    if positive_sum >= 2:
        # Return True if at least two arguments are positive
        return True
    else:
        # Return False if fewer than two arguments are positive
        return False

print(positive_count(10, -5, 2))