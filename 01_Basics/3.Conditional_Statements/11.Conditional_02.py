# BMI Calculator

# Body Mass Index (BMI) is a simple measure that helps determine whether a person's weight is appropriate for their height
# Write a Python program that takes the height(in m) and weight (in kg) as input from the user and displays the corresponding weight category using the following rules:

# BMI Value Category
# Less than 18.5 --> Underweight
# 18.5 to 24.9 --> Normal weight
# 25.0 to 29.9 --> Overweight
# 30.0 or above --> Obese

weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in m): "))

BMI = (weight) / ((height)**2)

if(BMI < 18.5):
    print("Underweight")
elif(BMI < 25):
    print("Normal Weight")
elif(BMI < 30):
    print("Overweight")
else:
    print("Obese")