
# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.
# Note: 1 square meter == 10.7639 square feet


length = int(input('What is the length in meters? '))
width = int(input('What is the width in meters? '))

print(f'The area in square meters is {length*width} m')
print(f'The area in square feet is {length*width*10.7639} ft')


# LS Solution (':.2f' is for formatting to two decimal places)

length = float(input("Enter the length of the room in meters: "))
width = float(input("Enter the width of the room in meters: "))

area_in_meters = length * width
area_in_feet = area_in_meters * 10.7639

print(f"The area of the room is {area_in_meters:.2f} "
      f"square meters ({area_in_feet:.2f} square feet).")