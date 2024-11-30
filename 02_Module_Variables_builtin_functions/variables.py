# Day 2: 30 Days of python programming

import datetime, math

# Exercise Level 1

first_name = 'Abdulsalam'
last_name = 'Idris'
full_name = f'{first_name} {last_name}'
country = 'Nigeria'
city = 'Kano'
age = 19
year = datetime.date.today().year
is_married = True
is_true = True
is_light_on = False
height, weight, size = 190, 70, 42


# Exercise Level 2

# Check the data type of all your variables using type() built-in function
variables = [first_name, last_name, full_name, country, city, age, year, 
             is_married, is_light_on, height, weight, size]

for var in variables:
    print(f'Data type of {var} is {type(var)} ')



# Using the len() built-in function, find the length of your first name
print(f'The lenght of {first_name} is {len(first_name)}')


# Compare the length of your first name and your last name
print(f'Lenght of first name {first_name} compared to last name {last_name} is {len(first_name) - len(last_name)} letters')


# Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4


#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(f'num_one {num_one} plus num_two {num_two} = {total}')

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(f'num_one {num_one} minus num_two {num_two} = {diff}')



# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
print(f'num_two {num_two} multiplied by num_one {num_one} = {product}')


# Divide num_one by num_two and assign the value to a variable division
division = num_one/num_two
print(f'num_one {num_one} divided by num_two {num_two} = {division}')


# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(f'Remainder for num_two {num_two} divided by num_one {num_one} = {remainder}')

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one**num_two
print(f'num_one {num_one} to the power of num_two {num_two} = {exp}')

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(f'Floor division of num_one {num_one} by num_two {num_two} = {floor_division}')


''' The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
'''
area_of_circle = math.pi * 30
circum_of_circle = 2 * math.pi * 30**2
print(f'Area of a circle with radius 30 meters is {area_of_circle:.2f} meter squared')
print(f'Circumference of a circle with radius 30 meters is {circum_of_circle:.2f} meters')


first_name_inp = input('Provide your first name:  ')
last_name_inp = input('Provide your last name:  ')
country_inp = input('Provide your preferred country')
age_inp = input('What is your age:  ')
print(f'{first_name_inp} {last_name_inp} is from {country_inp}, and is {age_inp} years old')


# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords