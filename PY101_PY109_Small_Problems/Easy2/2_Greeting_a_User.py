# Write a program that asks for user's name, then greets the user. 
# If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).


# Example 1
# What is your name? Sue
# Hello Sue.

# Example 2
# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?


name = input('Please provide your name: ')
if '!' in name:
    print(f'HELLO {name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {name}.')


# LS Solution

name = input('What is your name? ')

if name.endswith("!"):
    print(f'HELLO {name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {name}.')
