import keyword

print("Hello!")

#Print Python Keywords
print(keyword.kwlist)
print(keyword.iskeyword("if"))
print(keyword.iskeyword("If"))

#Variable
a=3
b=4
print(a+b)

name="John"
age=30
salary=50000.50
email="john@example.com"
conNum=3+5j
isAdult=True
my_list=[2,3.2,True,"Hello "]
my_tuple=(1,2,3,4,"Hello")
my_set={1,2,3,4,5,True,3+5j}
my_dict={
    "name":"John",
    "age":30,
    "salary":50000.50
} 
#type is used to check the data type of a variable
print(name,type(name))
print(age,type(age))
print(salary,type(salary))
print(email,type(email))
print(conNum,type(conNum))
print(isAdult,type(isAdult))
print(my_list,type(my_list))
print(my_tuple,type(my_tuple))
print(my_set,type(my_set))
print(my_dict,type(my_dict))

#Type Casting
#Implicit Type Casting
x=10
y=32.5
z=x+y
print(z,type(z))

#Explicit Type Casting
name="John"
age=30
# msg="My name is "+name+" and I am "+age+" years old."
# print(msg)

msg="My name is "+name+" and I am "+str(age)+" years old."
print(msg)

#Inbuild Functions
# x=10
# int(x)
# float(x)
# str(x)
# bool(x)
# complex(x)
# list(x)
# tuple(x)
# set(x)