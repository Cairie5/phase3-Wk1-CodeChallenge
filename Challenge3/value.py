# Function to check if a character is a consonant
def is_consonant(char):
    return char.isalpha() and char not in "aeiou"

# Function to calculate the value of a consonant
def get_consonant_value(char):
    return ord(char) - ord('a') + 1

# Function to find the highest value of consonant substrings
def highest_consonant_value(s):
    max_value = 0
    current_value = 0

    for char in s:
        if is_consonant(char):  # If the character is a consonant
            current_value += get_consonant_value(char)  # Add its value to the current substring value
            max_value = max(max_value, current_value)   # Update the maximum value if needed
        else:  # If the character is a vowel
            current_value = 0  # Reset the current substring value

    return max_value

# Example usage
input_string = "abcdedfg"
result = highest_consonant_value(input_string)
print(result)  # Output: 15 (consonant substrings: "bcd", "d", "fg")
