
# Write a function that takes a positive integer, n, as an argument 
# and prints a right triangle whose sides each have n stars. 
# The hypotenuse of the triangle (the diagonal side in the images below) 
# should have one end at the lower-left of the triangle, and the other end at the upper-right.

# Example 1
# triangle(5)

# Output

#     *
#    **
#   ***
#  ****
# *****

# Example 2
# triangle(9)

# Output

#         *
#        **
#       ***
#      ****
#     *****
#    ******
#   *******
#  ********
# *********


def triangle(length):
    index = 0
    while index < length:
        for idx in range(length):
            print((' ' * (length - (idx + 1))) + ('*' * (idx + 1)))
            index += 1

triangle(9)


# LS Solution

def triangle(height):
    for num in range(1, height + 1):
        spaces = height - num
        stars = num
        print(f'{" " * spaces}{"*" * stars}')
