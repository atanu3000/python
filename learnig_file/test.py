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

# st = 'Print only the words that start with s in this sentence'

# for ch in st.split():
#     if ch[0] == 's':
#         print(ch)

#  <--------- Animal Crackers --------->
# def animal_cracker(str):
#     str = str.split()
#     # print(str[0][0])
#     # print(str[1][0])
#     if str[0][0] == str[1][0]:
#         return True
#     else:
#         return False

# print(animal_cracker('Levelheaded Llama'))

# print(animal_cracker('Crazy Kangaroo'))

# def almost_there(num):
#     if num >= 90 and num <= 110:
#         return True
#     elif num >= 190 and num <= 210:
#         return True
#     else:
#         return False

# print(almost_there(104))
# print(almost_there(150))
# print(almost_there(209))

# def has_33(nums):
#     i = 0
#     for num in nums:
#         if num == 3:
#             if nums[i+1] == 3:
#                 return True
#             else:
#                 return False
#         i += 1

# list = [3, 1 , 3]
# print(has_33(list))

# a = 13
# b = 3

# add = a + b
# sub = a - b
# mul = a * b
# div1 = a / b
# div2 = a // b
# mod = a % b
# power = a ** b

# print(add)
# print(sub)
# print(mul)
# print(div1)
# print(div2)
# print(mod)
# print(power)

# a = 10
# b = a
# print(a)

# b += a
# print(b)

# b -= a
# print(b)

# b *= a
# print(b)

# b <<= a
# print(b)

# a = 10
# b = 30

# print(a > b)

# print(a < b)

# print(a == b)

# print(a != b)

# print(a >= b)

# print(a <= b)

# a = True
# b = False
# x = 10

# print(a and b)
  
# print(a or b)
  
# print(not a)

# print(x < 5 and a < 15)
# print(x < 5 or a < 15)
# print(not(x < 5 and a < 15))

# a = 10
# b = 20
# c = a
  
# print(a is not b)
# print(a is c)

# a = 10
# b = 4

# print(a & b)

# print(a | b)

# print(~a)

# print(a ^ b)

# print(a >> 2)

# print(a << 2)

# x = 24
# y = 20
# list = [10, 20, 30, 40, 50]
  
# if (x not in list):
#     print("x is NOT in list")
# else:
#     print("x is in list")
  
# if (y in list):
#     print("y is in list")
# else:
#     print("y is NOT in list")

# list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(list)
# for i in list:
#     for j in i:
#         print(j, " ", end="")
#     print()

############## with using init ##############

# class node:
#     def __init__(self, a , b):
#          self.a = a
#          self.b = b 
#     def sum(self):
#         return self.a + self.b

# res = node(2,5).sum() 
# print(res)

############## without using init ##############

# class node:
#     def sum(self, a, b):
#         self.a = a
#         self.b = b
#         return(self.a + self.b)

# res = node().sum(10,20)
# print(res)

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0 :
#         print("Fizz")
#     elif number % 5 == 0 :
#         print("Buzz")
#     else: 
#         print(number)
        

# x = 29
# print(x >> 1)

# a = 10
# b = -a
# print(b)

# print("atanu\n" * 10 )

# if __name__ == main:
#     print("yes")
# else:
#     print("no")

# class Employee:
#     promotion = 1.04
#     def __init__(self, f_name, l_name, pay):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.email = f_name + "." + l_name + "@gmail.com"
#         self.pay = pay
#         self.promotion = Employee.promotion
    
#     def apply_raise(self):
#         self.promotion = 1.05
#         self.pay *= self.promotion
    
# emp_1 = Employee("atanu", "paul", 60000)
# emp_2 = Employee("rohit", "mondal", 50000)

# # print(emp_1.__dict__)
# # print(emp_2.__dict__)

# # print(emp_1.pay)
# emp_1.apply_raise()
# # print(emp_1.pay)

# print(emp_1.promotion)
# print(emp_2.promotion)
# print(emp_1.__dict__)
# print(emp_2.__dict__)
# # print(emp_1.promotion)

# # emp_1.promotion = 1.05
# # print(emp_1.__dict__)


