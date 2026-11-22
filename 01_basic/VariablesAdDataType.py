print("Hello World!!")

#Variable initialization
name="Sushmita"
age=32
city="Pune"

print("Hi", name)
print("Age", age)
print("Lives in", city )

print("My name is "+ name + " Age "+ str(age)+ " Lives in "+ city)

#Single assignment
a=10
b=30
c=6.6

print("a", a)
print("b", b)
print("c", c )

#Multiple assignment
x,y,z=10,20,"Hello"

print("x", x)
print("y", y)
print("z", z)

#Same value to multiple variable
a=b=c=100

print("a", a)
print("b", b)
print("c", c )

#Printing variable values
firstName="Sushmita"
print('hello world & my name is pranit') # single value -> but fixed value
print(firstName) # single value

print('My','name is',firstName) #Dynamic values

#type is used to check the data type of a variable
age = 10
print("Type age varible : ", type(age))

percentage = 10.3
print("Type of percentage variable : ", type(percentage))

cmplx = -10.3 + 5j
print("Type of cmplx variable : ", type(cmplx))

name = '''pranit'''
print("Type of name variable : ", type(name))

e = True
print("e : ", type(e))

#None is a special data type in python which represents the absence of value or a null value.
aVariable = None