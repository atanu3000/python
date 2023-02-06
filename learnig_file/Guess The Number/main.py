from art import logo
print(logo)
print("Guess the number between 1 to 100: ")
level = input("Choose the difficulty level. Type 'easy' or 'hard': ").lower()
num_level = {"easy": 10, "hard": 5}

final_goal = 35
attempts = num_level[level]

while attempts > 0:
    guess = int(input(f"You have {attempts} attempts remaining to guess the number: "))
    if guess == final_goal:
        print("You Win")
        break
    elif guess < final_goal:
        print("Too Small.")
        attempts -= 1
    else:
        print("Too Big.")
        attempts -= 1