
# Write a program that asks the user to enter an integer greater than 0 
# then asks whether the user wants to determine the sum or the product 
# of all numbers between 1 and the entered integer, inclusive.

# Example 1:
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s
# The sum of the integers between 1 and 5 is 15.

# Example 2:
# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p
# The product of the integers between 1 and 6 is 720.


import math

integer = int(input('Please enter an integer greater than 0: '))
sum_or_product = input('Enter "s" to compute the sum, or "p" to compute the product. ')

range_of_numbers = range(1,(integer+1))
product_of_numbers = math.prod(range_of_numbers)


if sum_or_product == 's':
    print(f'The sum of the integers between 1 and {integer} is {sum(range_of_numbers)}.')
elif sum_or_product == 'p':
    print(f'The sum of the integers between 1 and {integer} is {product_of_numbers}.')
else:
    print('Please input either s or p')


# LS Solution

def compute_sum(target_num):
    return sum(range(1, target_num+1))

def compute_product(target_num):
    result = 1
    for num in range(1, target_num+1):
        result *= num
    return result

number = int(input('Please enter an integer greater than 0: '))
operation = input('Enter "s" to compute the sum, or "p" to compute the product: ')

if operation == 's':
    print(f'The sum of the integers between 1 and {number} is {compute_sum(number)}.')
elif operation == 'p':
    print(f'The product of the integers between 1 and {number} is {compute_product(number)}.')
else:
    print('Oops. Unknown operation.')