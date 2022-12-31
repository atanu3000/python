import random
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
'V', 'W', 'X', 'Y', 'Z']
symbol_list = ['!', '@', '#', '%', '^', '&', '*', '(', ')']
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to password generator!")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

    # <-----------Easy Level----------->
# password = " "

# for char in range(1, letters + 1) :
#     password += random.choice(letter_list)

# for char in range(1, symbols + 1) :
#     password += random.choice(symbol_list)

# for char in range(1, numbers + 1) :
#     password += random.choice(number_list)

# print("Your password: " + password)

   # <-----------Hard Level----------->
password_list = []

for char in range(1, letters + 1) :
    password_list.append(random.choice(letter_list))

for char in range(1, symbols + 1) :
    password_list += random.choice(symbol_list)

for char in range(1, numbers + 1) :
    password_list += random.choice(number_list)

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = " "
for char in password_list:
    password += char

print("\nYour password: " + password)