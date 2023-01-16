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

# def add(a, b):
#     return a + b
# def sub(a, b):
#     if a > b:
#         return a - b
#     else:
#         return b - a
    
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# c = add(a, b)
# print(f"addition: {c}")
# d = sub(a, b)
# print(f"difference: {d}")

# import math
# a, b = 40, 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(math.ceil(a/b))
# print(round(a/b))
# print(a//b)
# print(a**b)

# programing_dictionary = {
#     "bug": "Video provides a powerful way to help you prove your point. ",
#     "bug1": "When you click Online Video, you can paste in the embed code for the video you want to add. ",
#     "bud2": "You can also type a keyword to search online for the video that best fits your document."
# }
# # print(programing_dictionary)
# for thing in programing_dictionary:
#     print(thing)
#     print(programing_dictionary[thing])

#   ----- distionary problems -----
# d = {'simple_key' : 'hello'}
# print(d['simple_key'])

# d = {'k1' : {'k2' : 'hello'}}
# print(d['k1']['k2'])

# d = {'k1': [{'nest_key' : ['this is deep',['hello']]}]}
# print(d['k1'][0]['nest_key'][1][0])

# d = {'k1' : [1, 2, {'k2': ['this is tricky', {'though' : [1, 2, ['hello']]}]}]}
# print(d['k1'][2]['k2'][1]['though'][2][0])

# list3 = [1,2,[3,4,'hello']]
# list3[2][2] = 'goodbye'
# print(list3)

# a = [1, 2, 3, 4]
# b = a[:]    # "[:]" is  means a new list is assigned in 'b' as same as 'a' 
# a[0] = 10
# print(a)
# print(b)

# l = [1, 2, 3, 4]
# print(*l)
# print(l[::])

st = 'Print only the words that start with s in this sentence'

for ch in st.split():
    if ch[0] == 's':
        print(ch)



# print("atanu\n" * 10 )

# if __name__ == main:
#     print("yes")
# else:
#     print("nO")