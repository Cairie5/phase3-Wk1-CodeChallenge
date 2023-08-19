def positive_count(a=10, b=-5, c=2):
    # Sum the positive numbers and check if the sum is greater than or equal to 2
    positive_sum = sum(num for num in (a, b, c) if num > 0)
    return positive_sum >= 2

result = positive_count(10, -5, 2)
print(result)
