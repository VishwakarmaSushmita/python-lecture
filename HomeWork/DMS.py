#Write a program that takes an input from user and checks whether the number is even or odd.
checkNum= int(input("Enter number to validate whether it is Even or Odd:"))
if checkNum%2 == 0:
    print(checkNum, "is Even number")
else:
    print(checkNum, "is Odd number")