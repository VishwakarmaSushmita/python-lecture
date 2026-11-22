#Add function
print("Add function")
def add(a,b) :
    result =  a+b
    return result

value = add(10,20)
print(value)

print("----------------------------------------------------")
print("Multiply function")
def multiply() :
    num1 = input("Enter first number: ")
    num1 = int(num1)
    num2 = input("Enter second number: ")
    num2 = int(num2)

    result = num1*num2

    return result

value = multiply()
print(value)

print("----------------------------------------------------")
#Q. write a function to take 3 parameters and subtract and divide
#subtract
print("subtract")
def substractoperation(num1, num2, num3):
    operation1 = num1 - num2 - num3
    return operation1

operationOutput = substractoperation(10,60, 20)

print("result:",operationOutput)
print("----------------------------------------------------")
print("Divide")
def divideOperation():
    num1 = input("Enter first number: ")
    num1 = int(num1)
    num2 = input("Enter second number: ")
    num2 = int(num2)
    operation1 = num1 / num2
    return operation1

operationOutput = divideOperation()

print("result:",operationOutput)
print("----------------------------------------------------")
print("function to take 3 parameters and subtract and divide")
def Operation(num1, num2, num3):
    operation1 = (num1 - num2 - num3)/num3
    return operation1

operationOutput = Operation(10,60, 20)

print("result:",operationOutput)

