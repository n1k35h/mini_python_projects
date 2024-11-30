height = float(input('Enter your Height in meter (e.g: enter 1.67 for 167cm): '))
weight = float(input('Enter your weight in kg: '))

bmi = round(weight / (height ** 2), 2)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}. You're in the underweight range")
elif bmi >= 18 and bmi <= 24.9:
    print(f"Your BMI is {bmi}. You're in the healthy weight range")
elif bmi >= 25 and bmi <= 29.9:
    print(f"Your BMI is {bmi}. You're in the overweight range")
elif bmi >= 30 and bmi <= 39.9:
    print(f"Your BMI is {bmi}. You're in the obese range")
else:
    print("Time to seek medicial advice!")

print("\n")
