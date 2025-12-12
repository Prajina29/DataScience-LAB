# 5. Define a function that takes two numbers as arguments, and returns their greatest
#common divisor (GCD).

try:
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print("GCD =", gcd(x, y))
except:
    print("Invalid input")
