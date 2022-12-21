print("Welcome to the love calcaltor!")
name1 = (input("Enter your name: ")).lower()
name2 = (input("Enter his/her name: ")).lower()

name = name1 + name2
# print(name1)
# print(name2)

score = 0

score1 = name.count("t")+name.count("r")+name.count("u")+name.count("e")
score2 = name.count("l")+name.count("o")+name.count("v")+name.count("e")

score = score1*10 + score2

if score < 10 or score > 90:
    print(f"Your score is {score}, You are like coke and mentos!")
elif score > 40 and score < 50:
    print(f"Your score is {score}, You are all right!")
else:
    print(f"Your score is {score}")