def exactly_two_positive(a, b, c):
    # Initialize a counter to keep track of positive numbers
    positive_count = 0
    
    # Check if 'a' is positive
    if a > 0:
        positive_count += 1  # Increment the positive count if 'a' is positive
        
    # Check if 'b' is positive
    if b > 0:
        positive_count += 1  # Increment the positive count if 'b' is positive
        
    # Check if 'c' is positive
    if c > 0:
        positive_count += 1  # Increment the positive count if 'c' is positive
        
    # Return True if exactly two numbers are positive, otherwise return False
    return positive_count == 2
# Test cases
print(exactly_two_positive(1, 2, 3))  # it returns True (2 positive numbers)
print(exactly_two_positive(-1, 0, 1)) # it returns  False (1 positive number)
print(exactly_two_positive(0, -2, 5)) # it returns True (2 positive numbers)
print(exactly_two_positive(0, 0, 0))  # it returns False (0 positive numbers)
print(exactly_two_positive(5, 6, -7)) # it returns False (2 positive numbers but 3 positive values)

