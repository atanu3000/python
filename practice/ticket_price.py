height = int(input("Enter your height: "))
bill = 0
if height > 120:
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
    elif age < 18:
        bill = 7
    else:
        bill = 12

    photo = input("Are you have photo ? Y or N : ")

    if photo == "Y" or photo == "y":
        bill += 3
    
    print(f"Your bill is ${bill}")

else:
    print("Cant't ride.")