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

# list = ['a', 'b', 'c', 'd', 'e']
# print(list.index('d'))

# list_1 = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']
# for i in list_1:
#     for j in i:
#         print(j, "", end="")
#     print()

# elm = input("Find the position of a element: ")

# # x = y = 0
# # a = b = 0
# # for i in list:
# #     y = 0
# #     for j in i:
# #         if j == elm:
# #             a, b = x ,y
# #         y += 1
# #     x += 1

# a = b = 0
# for i in list_1:
#     list_2 = list(i)
#     if elm in list_2:
#         b = list_2.index(elm)
#         break
#     a += 1
        
# print("\nsearch for: ", elm)

# for i in range(b):
#     print(list_1[a][i], "", end="")

# print()

# for i in range(a):
#     print(list_1[i][b], "", end="")

# def add_user():
#     n = int(input("Enter number of user: "))
#     dic = {}
#     for i in range(1, n+1):
#         dic1 = {}
#         dic1['name'] = input(f"{i}. User name: ")
#         dic1['id'] = input(f"     User id: ")
#         dic[i] = dic1
    
#     for row in dic:
#         print(dic[row])

# add_user()

# lower_list =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'l', 'm',
# 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# upper_list = [i.upper() for i in lower_list]

# import string

# alphabet = string.ascii_lowercase
# print(alphabet)
# l_list = list(str(alphabet))
# print(l_list)
# # alphabet = list(alphabet)
# # # print(upper_list)
# # print(l_list)
# # res = ""
# # for i in lower_list:
# print(type(alphabet))
# print(type(l_list))

# python program to convert into decimal number system
# s1 = "17"
# s2 = "1110010"
# s3 = "1c2"
 
# n1 = int(s1, 8)
# print('Octal 17 = ', n1)
# n2 = int(s2, 2)
# print('Binary 1110010 = ', n2)
# n3 = int(s3, 16)
# print('Hexadecimal 1c2 = ', n3)

# n = int(100,2)
# print(n)

######### IMPORTANT CODES #########

# a = 10
# b = bin(a)
# print(b[2::])

# print(type(b))

# import math as m
# a = m.ceil(4.0)
# print(a)
# a = m.(4.0)
# print(a)

# a = "atanu"
# # b = "12345678"
# print(b[:-len(b)+1:-1])
# print(b[2::])
# print(len(a))

# ------------------- Factorial using recursion -------------------

# def fact(num):
#     if num == 0 or  num == 1:
#         return 1
#     return num * fact(num-1)

# print(f'Factorial = {fact (int (input ("Enter a number: ") ) ) }')

# ------------------- Exponenstial -------------------

# def exp(base, pow):
#     if pow == 0:
#         return 1
    
#     return base * exp(base, pow-1)

# print(f'Answer: {exp(int(input("Enter base: ")), int(input("Enter power: ")))}')

# ------------------- Fibonacci Series -------------------

# def fibonacci(n):
#     # pass
#     if n <= 1:
#         return n
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))
    
# term = int(input("Enter the term: "))

# if term <= 0:
#     print("Enter any positive integer")
# else:
#     print("Fibonacci Sequence: ")
#     for i in range(term):
#         print(fibonacci(i), "",end="")

# ------------------- GCD of a number -------------------

# def gcp(a, b):
#     if b == 0:
#         return a
#     return gcp(b, a%b)

# print(f'GCP is: {gcp(int(input("Enter first num: ")), int(input("Enter second num: ")))}')

# def volume(l, b = 5, h = 7):
#     vol = l * b * h
#     return vol

# ans = volume(10)
# print("The volume is: ", ans)
    
# from math import pi, sqrt
# print(round(pi, 2))
# print(int(sqrt(81)))

# import sys
# a = int(sys.argv[1])
# b = int(sys.argv[2])

# sum = a + b
# print("Sum = ", sum)

# print(sys.argv)

# import __builtin__
# print(dir(__builtin__))

# print(dir(__builtins__))
# print(__name__)
# if __name__ == '__main__':
#     print("Hello World")

# with open('swap.py', 'w') as s:
#     s.write("import test\n")
#     s.write("print(f'The module name is: {__name__}')")

# import os
# os.rename('swap.py', 'swap_num.py')
# print("File renamed")

# os.rmdir('file.py')

# a = 'Hello'
# index = 0
# for i in a:
#     print(f'a[{index}] = {i}')
#     index += 1

# s = set()
# print(type(s))
# s = {1, 2, 3, 4}
# print(type(s))
# s = set([1,2,3])
# print(type(s))
# print(s)

# list = [1, 1, 2, 2, 2, 3, 4, 4]
# # print(list)

# # print(set(list))

# set = set(list)
# print(set)

# set.add(5)
# # set.add([6, 7])  # this is a type error
# set.update([6, 7])
# print(set)

# dict = {1: 'a', 2: 'b', 3: 'c', 2: 'd'}
# # print(dict)

# dict2 = dict
# print(dict2)

# dict = {1: 'A', True: 'B', 2: 'C', 3: 'D'}
# dict = {1: 'a', 1: 'b'}

# print(dict[1])

# print(hash(1))
# print(hash(True))
# # dict.clear()

# dict2 = dict.copy()

# print(dict2)
# print(dict2.items())
# print(dict2.values())

# for items in dict:
#     print(dict[items])


# dict.clear()
# print(dict)

# class demo:
#     num = 10

#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

# print(demo.num)

# s1 = demo('Atanu', 58)
# print(s1.name, s1.roll)

# class demo: 
#     x = 10
#     def __init__ (self, name, roll):
#         self.name = name
#         self.roll = roll
#         self.x = 100

# print(demo.x)

# s1 = demo('Atanu', 58)
# print(s1.x)
# print(s1.name)
# print(s1.__dict__)

from os import *
from sys import *
from collections import *
from math import *

def findAddedCharacter(s, t):
    # Write your code here.
    # pass
	for item in t:
		if item not in s:
			return item

# Main.
test = int(input())
for x in range(test):
	s = input()
	t = input()
	print(findAddedCharacter(s, t))
