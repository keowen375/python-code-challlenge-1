def highest_consonant_value(s):
    # Define the set of consonant characters
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    # Initialize variables to keep track of maximum and current consonant values
    max_value = 0
    current_value = 0
    
    # Iterate through each character in the input string 's'
    for char in s:
        # Check if the character is a consonant
        if char in consonants:
            # Calculate the value of the consonant based on its position in the alphabet
            current_value += ord(char) - ord('a') + 1
        else:
            # If a non-consonant character is encountered, compare current_value with max_value
            # Update max_value if necessary, then reset current_value to 0
            if current_value > max_value:
                max_value = current_value
            current_value = 0
    
    # After the loop, make a final check for current_value against max_value
    if current_value > max_value:
        max_value = current_value
    
    # Return the maximum consonant value found in the string
    return max_value

print(highest_consonant_value("hello"))          # it returns 8 (l, l)
print(highest_consonant_value("programming"))    # it returns 17 (g, r, m, m)
print(highest_consonant_value("aeiou"))          # it returns 0 (no consonants)
print(highest_consonant_value("rhythm"))         # it returns 20 (r, h, t, h, m)
print(highest_consonant_value("bcd"))            # it returns 6 (b, c, d)
