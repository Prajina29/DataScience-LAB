#b. A program that computes the Body Mass Index (BMI) of a user, taking their height and weight as input. The program should allow the user to enter their
#height in either feet/inches or centimeters and their weight in either kilograms or pounds.
#Extend the program to convert BMI into a category based on standard criteria:
#■ Underweight: < 18.5
#■ Normal weight: 18.5 - 24.9
#■ Overweight: 25 - 29.9
#■ Obese: ≥ 30

def BMI(weight, height):
    # BMI formula: weight (kg) / (height (m))^2
    bmi = weight / (height ** 2)
    return bmi

# Weight input
print("Enter your weight:")
print("1. Kilograms (kg)")
print("2. Pounds (lbs)")
weight_choice = int(input("Enter your choice (1 or 2): "))

if weight_choice == 1:
    weight_kg = float(input("Enter weight in kg: "))
elif weight_choice == 2:
    weight_lbs = float(input("Enter weight in pounds: "))
    weight_kg = weight_lbs * 0.453592  # Convert pounds to kg
else:
    print("Invalid choice")
    exit()

# Height input
print("Enter your height:")
print("1. Feet and inches")
print("2. Inches")
print("3. Centimeters")
height_choice = int(input("Enter your choice (1, 2, or 3): "))

if height_choice == 1:
    feet = float(input("Enter feet: "))
    inches = float(input("Enter inches: "))
    height_m = (feet * 12 + inches) * 0.0254  # Convert to meters
elif height_choice == 2:
    inches = float(input("Enter height in inches: "))
    height_m = inches * 0.0254
elif height_choice == 3:
    cm = float(input("Enter height in cm: "))
    height_m = cm / 100
else:
    print("Invalid choice")
    exit()

bmi = BMI(weight_kg, height_m)
print(f"Your BMI is: {bmi:.2f}")

