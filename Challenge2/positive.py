# Define a function named positive_count with three arguments: a, b, and c.
def positive_count(a, b, c):
   
    # Create a count variable to keep track of the number of positive integers.
    count = 0
    
    # Check if the first integer 'a' is positive.
    if a > 0:
        count += 1
    
    # Check if the second integer 'b' is positive.
    if b > 0:
        count += 1
    
    # Check if the third integer 'c' is positive.
    if c > 0:
        count += 1
    
    # Check if exactly two out of the three integers are positive.
    if count == 2:
        return True
    else:
        return False


print(positive_count(2, 4, -3))   # True
print(positive_count(-4, 6, 0))   # False
