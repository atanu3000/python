# age = input("Enter age here: ")
# print(type(age))

# year = print(input("Enter the year: "))

# import random

# random_int = random.randint(0, 1)
# print(random_int)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# a = ["a", "b", "c", "d"]
# # (a.append("z"))/
# a.extend(["e", "f", "g"])
# print(a)

# name = input("Enter the names: ")
# print(name)

# fruits = ["apple", "mango", "lemon", "grape"]
# for fruit in fruits:
#     print(fruit)

# height = input("Inout a list of student heights: ").split()
# for n in range(0, len(height)):
#     height[n] = int(height[n])
# print(height)

# max = 0
# for h in height:
#     type(h)
#     if int(max) < int(h):
#         max = h

# print(f"Max: {max}")

# total = 0
# for num in range(1, 101, 2):
#     # if num %2 == 0:
#     print(num)
#     total += num


# print(f"Total of even numbers: {total}")

# count = 5
# while count > 0:
#     print(count) 
#     count -= 1

def add(a, b):
    return a + b
def sub(a, b):
    if a > b:
        return a - b
    else:
        return b - a
    
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = add(a, b)
print(f"addition: {c}")
d = sub(a, b)
print(f"difference: {d}")




