# 1) WAP that takes two numbers as input from the user and print their sum.

a = input("Enter first number: ")
b = input("Enter second number: ")

try:
    a = float(a)
    b = float(b)
    sum = a+b

    if sum.is_integer():
        sum = int(sum)

    print("Sum is:", sum)

except ValueError:
    print("Invalid Input")