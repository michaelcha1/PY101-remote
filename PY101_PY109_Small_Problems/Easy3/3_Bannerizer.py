
# Write a function that takes a short line of text and prints it within a box.

# Example 1
# print_in_box('To boldly go where no one has gone before.')

# Output

# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

# Example 2
# print_in_box('')

# Output

# +--+
# |  |
# |  |
# |  |
# +--+


def print_in_box(text):
    print('+' + ('-'*(len(text)+2)) + '+')
    print('|' + (' '*(len(text)+2)) + '|')
    print('| ' + text + ' |')
    print('|' + (' '*(len(text)+2)) + '|')
    print('+' + ('-'*(len(text)+2)) + '+')

print_in_box('To boldly go where no one has gone before.')


# LS Solution

def print_in_box(message):
    horizontal_rule = f'+-{"-" * len(message)}-+'
    empty_line = f'| {" " * len(message)} |'

    print(horizontal_rule)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(horizontal_rule)

