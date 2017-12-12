# Tinh chi so BMI

weight = float(input("Enter your weight (in pounds): "))
height = float(input("Enter your height (in inches): "))

BMI = (weight * 0.45359237) / (height * 0.0254)
if BMI < 18.5:
    print("Underweight")
elif 18.5 < BMI < 25.0:
    print("Normal")
elif 25.0 < BMI < 30.0:
    print("Overweight")
else:
    print("Obese")

#This is command line
print("Say hello!")