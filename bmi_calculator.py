height = float(input("enter your hight in m: "))
weight = float(input("enter your weight in kg: "))

person = round(weight / height ** 2)



if person < 18.5:
    print(f"Your BMI is {person}, you are underweight.")
elif person < 25:
    print(f"Your BMI is {person}, you are normal weight.")
elif person < 30:
    print(f"Your BMI is {person}, you are overweight.")
elif person < 35:
    print(f"Your BMI is {person}, you are obese.")
else:
    print(f"Your BMI is {person}, you are clinically obese.")