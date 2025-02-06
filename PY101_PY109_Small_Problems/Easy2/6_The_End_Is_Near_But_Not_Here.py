
# Write a function that returns the next to last word in the string argument.
# Words are any sequence of non-blank characters.
# You may assume that the input string will always contain at least two words.


def penultimate(words):
    return words.split(' ')[-2]

print(penultimate('Launch School is great!'))


# LS Solution

def penultimate(words):
    words_list = words.split()
    return words_list[-2]

