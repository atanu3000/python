import random
print("Welcome to Rock Paper Scissors games!")

user = int(input(" 1. Rock\n 2. Paper\n 3. Scissors\n Choose: "))
comp = random.randint(1, 3)

choice = ["Rock", "Paper", "Scissor"]

print("You: " + choice[user-1])
print("Computer: " + choice[comp-1])

if user == 1 and comp == 2 or user == 2 and comp == 3 or user == 3 and comp == 1:
    print("Computer win!")
elif user == 1 and comp == 3 or user == 2 and comp == 1 or user == 3 and comp == 2 :
    print("You win!")
else:
    print("Try again")