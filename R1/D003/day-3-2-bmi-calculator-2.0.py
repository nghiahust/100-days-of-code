height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)
print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("Your are under weight")
elif bmi < 25:
    print("Your are normal weight")
elif bmi < 30:
    print("Your are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("Your are clinically obese")