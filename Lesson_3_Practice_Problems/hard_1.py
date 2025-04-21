# Question 1 - Will the following functions return the same results?

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# They do not return the same thing - the function first() returns the expected value of { prop1: "hi there" }
# second() returns None without throwing any errors, the indented block after the return is unreachable so nothing is returned


# Question 2 - What does the last line in the following code output?

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

# [1, 2]
# {'first': [1, 2]}

# Since num_list is a reference to the original list in dictionary, appending to num_list modifies the list. 
# Thus, the original dictionary is also updated.

# If, instead of modifying the original dictionary, we want to modify num_list but not dictionary, we have a couple of options:
# We can initialize num_list with a reference to a copy of the original list:

dictionary = {"first": [1]}
num_list = dictionary["first"].copy()
num_list.append(2)

# We can use list slicing which returns a new list:

dictionary = {"first": [1]}
num_list = dictionary["first"][:]
num_list.append(2)


# Question 3 - Given the following similar sets of code, what will each code snippet print?

# A)

def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# Output - Since variables one, two, and three in the mess_with_vars function are local, reassigning them does not affect the original lists:
one is: ['one']
two is: ['two']
three is: ['three']

# B)

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# Output - Again, the local variables in the mess_with_vars function are being reassigned, but this doesn't change the original lists:
one is: ['one']
two is: ['two']
three is: ['three']

# C)

def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# Output - In this case, the mess_with_vars function modifies the content of the lists directly. Since lists in Python are mutable and passed by object reference, the changes are reflected outside the function:
one is: ['two']
two is: ['three']
three is: ['one']


# In all three scenarios, the variables one, two, and three inside the mess_with_vars function are local to the function. 
# They are not the same as the variables one, two, and three defined outside the function. 
# This is known as variable shadowing, where the local variables inside the function overshadow the variables outside the function with the same names.


# Question 4 - Ben was tasked to write a simple Python function to determine whether an input string is an IP address using 4 dot-separated numbers, e.g., 10.4.5.11.
# Alyssa supplied Ben with a function named is_an_ip_number. It determines whether a string is a numeric string between 0 and 255 as required for IP numbers and asked Ben to use it. Here's the code that Ben wrote:

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True

# Alyssa reviewed Ben's code and said, "It's a good start, but you missed a few things. 
# You're not returning a false condition, and you're not handling the case when the input string has more or less than 4 components, e.g., 4.5.5 or 1.2.3.4.5: both those values should be invalid."

# Help Ben fix his code.

# To determine whether there are precisely 4 dot-separated "words" in the string, you can check the length of dot_separated_words after splitting the string:

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False

    while dot_separated_words:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True

# Great! The code now handles inputs that don't contain 4 dot-separated words, but the other error remains: it doesn't return False when encountering an invalid component such as 257 or abc. 
# Ben used a break statement to break out of the while loop, which caused control to fall through to the return True statement. 
# You can fix this by using return False instead of break:

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False

    while dot_separated_words:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True


# Question 5 - What do you expect to happen when the greeting variable is referenced in the last line of the code below?

if False:
    greeting = "hello world"

print(greeting)

# In Python, referencing an uninitialized variable will result in a NameError being raised. 
# This is because the if block is not executed due to the False condition, and hence, the greeting variable is never initialized.