print("Welcome to Treasure Island!")
print("Your mission is to find the Treasure.")

direction = input("Choose direction(Left or Right): ").lower()
if direction == "left":
    step = input("Choose nest step (swim or wait): ").lower()
    if step == "wait":
        door = input("Choose the door colour (Red, Yellow or Blue: ").lower()
        if door == "red":
            print("It's a room full of fire. Game Over!")
        elif door == "yellow":
            print("You found the Treasue, You Win!")
        elif door =="blue":
            print("You enter a room of Beast, Game Over!")
        else: 
            print("You chose a door doesn't exist, Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")