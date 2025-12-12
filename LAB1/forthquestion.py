# WAP that prints the Fibonacci series up to n terms.
try: 
    n = int(input("Enter the number of terms: "))

    a, b = 0, 1

    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci series up to 1 term:")
        print(a)
    else:
        print(f"Fibonacci series up to {n} terms:")
        print(a, b, end=' ')
        for _ in range(2, n):
            c = a + b
            print(c, end=' ')
            a, b = b, c
except:
    print("Enter a valid input")
