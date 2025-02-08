
# Write a function that takes a string argument and returns a new string that 
# contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

# These examples should all print True

# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')


def crunch(string):
    final_string = ''
    prev_char = None

    for char in string:
        if char != prev_char:
            prev_char = char
            final_string += char

    return final_string

print(crunch('ddaaiillyy ddoouubbllee'))


# LS Solution

def crunch(text):
    index = 0
    crunched_text = ''

    while index < len(text):
        if index == len(text) - 1 or text[index] != text[index + 1]:
            crunched_index += text[index]
        index += 1

    return crunched_text