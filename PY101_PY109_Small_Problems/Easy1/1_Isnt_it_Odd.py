
# Write a function that takes one integer argument 
# and returns True when the number's absolute value is odd, False otherwise.


def odd(integer):
    if abs(integer) % 2 == 1:
        return True
    else:
        return False
    

# LS Solution #

def is_odd(number):
    return abs(number) % 2 == 1


print(is_odd(-5))


