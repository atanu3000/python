import random
names = input("Give every bodies name: ")
name_str = names.split(", ")
random_choice = random.randint(0, len(name_str)-1)
print(name_str[random_choice] + " is going to but the meal today")