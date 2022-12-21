print("Welcome to the Tip Calculator!")
t_bill = float(input("What was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10, 12 or 15 ? "))
man = int(input("How many people to the split the bill? "))

amount = (t_bill / man) + (t_bill / man)*tip/100

print(f"Each person should pay: ${round(amount, 2)}")