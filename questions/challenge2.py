"""
    Challenge 2: Two numbers are positive.
    
    Task:
        Your job is to write a function, which takes three 
        integers a, b, and c as arguments, and returns True 
        if exactly two of of the three integers are positive 
        numbers (greater than zero), and False - otherwise.

    Examples:
        (2, 4, -3) == True

        (-4, 6, 8) == True

        (4, -6, 9) == True

        (-4, 6, 0) == False

        (4, 6, 10) == False

        (-14, -3, -4) == False
"""


def check_params_contain_two_positive_numbers(a, b, c):
    """
        Takes three integers a, b, and c as arguments, and returns True 
        if exactly two of of the three integers are positive numbers 
        (greater than zero), and False - otherwise.
    """
    num = 0
    if a > 0:
        num += 1
    if b > 0:
        num += 1
    if c > 0:
        num += 1

    if num == 2:
        return True

    return False
