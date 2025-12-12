# ODD or even check 
try:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
except:
    print ("Enter a valid input")
