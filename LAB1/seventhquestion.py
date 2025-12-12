# 7. Write a program that takes a list of numbers as input, and returns the largest number in
#the list.
try:
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    if numbers:
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
        print("The largest number is:", largest)
    else:
        print("The list is empty")
except :
    print ("Enter a valid input")

