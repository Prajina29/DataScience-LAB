#c. A program that checks if a user is eligible for army entrance based on their BMI
#and age. The eligibility criteria are as follows:
#■ Age must be between 18 and 40 years.
#■ BMI must be within the range of 18.5 to 29.9.

from bmi import bmi

def check_army(age, bmi):
    if 18 <= age <= 40 and 18.5 <= bmi <= 29.9:
        return f"Eligible for army entrance! Your BMI is {bmi:.2f}."
    else:
        return f"Not eligible. Your BMI is {bmi:.2f} and age is {age}."

age = int(input("Enter your age in years: "))

result = check_army(age, bmi)
print(result)
