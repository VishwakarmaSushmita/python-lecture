# is: Returns True if two variables refer to the same object(or value). 
a = [1, 2, 3]
b = a
print(a is b) # True

# is not: Returns True if two variables refer to different objects(or value)
a = [1, 2, 3]
b = [1, 2, 3]
print(a is not b) # True

#Identity Operators
# is not: Returns True if two variables refer to different objects(or value)
a = 10
b = 20
print("a is not b :", a is not b)

# is: Returns True if two variables refer to the same object(or value).
c = a

print("c is a :",c is a)