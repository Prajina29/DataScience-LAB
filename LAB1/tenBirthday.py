#10. Write multiple python files with separate functions for the following cases:
#a. A program that takes the age of an user, and gives their birth year, and if birth year was a leap year.
#b. A program that computes the Body Mass Index (BMI) of a user, taking their height and weight as input. The program should allow the user to enter their
#height in either feet/inches or centimeters and their weight in either kilograms or pounds.
#Extend the program to convert BMI into a category based on standard criteria:
#■ Underweight: < 18.5
#■ Normal weight: 18.5 - 24.9
#■ Overweight: 25 - 29.9
#■ Obese: ≥ 30
#c. A program that checks if a user is eligible for army entrance based on their BMI
#and age. The eligibility criteria are as follows:
#■ Age must be between 18 and 40 years.
#■ BMI must be within the range of 18.5 to 29.9.

# a) Answer

from datetime import date

def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

age = int(input("Enter your age: "))

current_year = date.today().year
birth_year = current_year - age

print("Your birth year is:", birth_year)

if is_leap_year(birth_year):
    print("Your birth year was a Leap year")
else:
    print("Your birth year was NOT a Leap Year ")