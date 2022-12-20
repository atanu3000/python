weight = int(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = round((weight / height ** 2),2)
print("BMI = " + str(bmi))

if(bmi < 18.5):
    print("Underweight")
elif(bmi <= 24.9):
    print("Healthy Weight")
elif(bmi <= 29.9):
    print("Overweight")
else:
    print("Obesity")