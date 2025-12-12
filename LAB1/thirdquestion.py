# WAP to print all prime numbers upto a given nunber n.

try:
    n = int(input("Enter a number: "))

    if n < 2:
        print(" No Prime numbers up to", n)
    else :
        print("Prime numbers up to", n, "are:")

        for num in range(2, n + 1):
            is_prime = True

            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(num)

except :
        print ("Enter a valid input")