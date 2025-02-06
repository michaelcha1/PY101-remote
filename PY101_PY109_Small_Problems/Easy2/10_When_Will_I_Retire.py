
# Build a program that displays when the user will retire and how many years she has to work till retirement.

# Example

# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!


from datetime import datetime

current_age = int(input('What is your current age? '))
retirement_age = int(input('At what age would you like to retire? '))

current_year = datetime.now().year
years_to_go = retirement_age - current_age
retirement_year = current_year + years_to_go

print(f"It's {current_year}. You will retire in {retirement_year}.")
print(f"You have only {years_to_go} years of work to go!")
