import random

special_char = list("!@#$%^&*()")
print(special_char)

def random_string(test_str):
    test_str = test_str.replace(" ", "")      # .replace("_", "")
    res = ''.join(random.choice((str.upper, str.lower))(char) for char in test_str)
    return res

def camelCase(name):
    new_name = ""
    for i in name.split(" "):
        new_name += i[0].upper()
        new_name += i[1:].lower()
        new_name += " "
    return new_name.split(" ")

def password_1(name, pet, year):
    # pass
    password = camelCase(name) + camelCase(pet) + str(year).split() + (random.choice(special_char)).split()
    random.shuffle(password)
    password = ''.join(password)
    print(f"password_1: {password}")

def password_2(name, pet, year):
    # pass
    password_list = random_string(name) + random_string(pet) + str(year)
    password_list = list(password_list)
    random.shuffle(password_list)
    password = ''.join(password_list)
    print(f"password_2: {password}")

name = input("Enter full name: ")
# name = "atanu paul"
pet = input("Enter your pet name: ")
# pet = "darlin"
bith_year = input("Enter your year of birth: ")
# bith_year = 2003
print()

while True:
    
    password_1(name, pet, bith_year)
    password_2(name, pet, bith_year)

    review = input("\nTry Again! 'y' for yes, 'n' for exit: ").lower()
    if review == 'n':
        break