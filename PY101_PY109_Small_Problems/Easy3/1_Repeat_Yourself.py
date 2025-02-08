
# Write a function that takes two arguments, a string and a positive integer, 
# then prints the string as many times as the integer indicates.

# Example
# repeat('Hello', 3)

# Output
# Hello
# Hello
# Hello


def repeat(string, number):
    for _ in range(number):
        print(string)

repeat('Hello', 3)
