# BMI Calculator

#input
name = input('Enter your name : ')
weight = input('Enter you weight (in kg) : ')
height = input('Enter your height (in ft) : ')

#process
heightInMeter = float(height) * 0.3048
bmi = float(weight) / heightInMeter**2

#output
print("\n--- BMI Result ---")
print("Name:", name)
print("Weight (kg):", weight)
print("Height (ft):", height)
print("BMI:", round(bmi, 2))
