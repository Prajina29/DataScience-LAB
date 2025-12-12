# Write a Program that checks if the given string is palindrom?

a = input("Enter a String ")

if a.isalpha():
    word = a.lower()

    if word == word[::-1]:
        print("String is Palindrome")
    else:
        print("Not a Plindrome")
else:
    print("Enter a Valid String")