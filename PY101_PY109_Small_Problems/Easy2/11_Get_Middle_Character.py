
# Write a function that takes a non-empty string argument and returns the middle character(s) of the string. 
# If the string has an odd length, you should return exactly one character. 
# If the string has an even length, you should return exactly two characters.

# Examples

# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True


def center_of(string):
    if len(string) % 2 == 1:
        center_index = len(string) // 2
        return string[center_index]
    else:
        left_index = len(string) // 2 - 1
        return string[left_index:left_index + 2]
    
print(center_of('Launch School is #1'))