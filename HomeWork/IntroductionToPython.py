'''create and print variables 
name
age
city'''

name= "John Doe"
age= 30
city= "New York"

print("Name:", name)
print("Age:", age)
print("City:", city)

print("--------------------------------------------------------")
#2. Create and Print Variables
'''a. Create variables to store:
Your favorite color
Your favorite food
Your favorite movie'''

favorite_color = "Blue"
favorite_food = "Pizza"
favorite_movie = "Avatar"

'''b. Print them in this format:

My favorite color is Blue
My favorite food is Pizza
My favorite movie is Avatar'''

print("My favorite color is", favorite_color)
print("My favorite food is", favorite_food)
print("My favorite movie is", favorite_movie)

#Try printing the information using multiple values inside print().
print("My favorite color is", favorite_color, ", My favorite food is", favorite_food, ", My favorite movie is", favorite_movie)

print("--------------------------------------------------------")
'''
3. Experiment with sep
Create three variables:

first = "Python"
second = "is"
third = "Easy"

Print them so that the output is:

Python---is---Easy
Condition: Use sep inside the print() function.'''

first = "Python"
second = "is"
third = "Easy"

print( first, second, third, sep="---")
print( first, second, third, sep="***")

print("--------------------------------------------------------")
'''4. Student Profile
Create variables for:

name
age
course
college
city
Print the information in one print() statement so that the output looks like:

Name: Pranit | 20 | Python | ABC College | Mumbai

Condition: Use sep to create the | separators.'''

name = "Alice"
age = 25
course = "Computer Science"
college = "ABC University"
city = "New York"

print(name,age,course,college,city,sep=" | ")

print("--------------------------------------------------------")
'''
5. Create an Output Using end
Create the following variables:

first_name = "Pranit"
last_name = "Gupte"

Write Python code that produces exactly:

My name is Pranit Gupte
I am learning Python
Python is interesting

Conditions:

Use end at least once.
Use variables for the first and last names.
Do not write the entire first line as one fixed string.
'''

firstname="John"
lastname="Doe"

print("My name is",firstname,lastname,end=".\n")
print("I am learning Python")
print("Python is interesting")

print("--------------------------------------------------------")
'''
6. Variable Naming Challenge
Look at the following variable names:
name
2name
first_name
first name
student123
class
my-name
_age
total_cost
'''

''' #Identify which names are valid Python variable names.
name
first_name
student123
my-name
_age
total_cost
'''
print("--------------------------------------------------------")
''' Identify which names are invalid.
2name: As per Python variable naming rules, variable names cannot start with a digit.
class: "class" is a reserved keyword in Python and cannot be used as a variable name.
first name: Variable names cannot contain spaces. '''
print("--------------------------------------------------------")
'''
For every invalid name, write a corrected version.
Then create variables using three of the valid names and print their values.

2name can be renamed as name2.
class can be renamed as class_name/className.
'''