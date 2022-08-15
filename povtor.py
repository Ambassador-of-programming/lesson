# int = 5, 10
# float = 3.5
# str = ''
# bool = True, False

# list = []
# tuple = ()
# set = {}
# dict = {1:1}

# if, elif, else, and, or, not
# + - * 

# a = list(range(star, stop, step))
# print(a)

# for i in range(24):
#         for j in range(60):
#             for second in range(60):
#             print(f"{i} чосов {j} минут {second} секунды")


# nums = [1,3,4,6,7,8,8,35,45,35,64,45,66,63,47,22,2,1]
# s = set(nums)
# nums_t = []
# for i in set(nums):
#     if nums.count(i) > 1:
#         a = (i, nums.count(i))
#         nums_t.append(a)
# print(nums_t)

# nums_t = [(i, nums.count(i)) for i in set(nums) if nums.count(i) > 1]
# print(nums_t)

# a = [1,4, [3,34,56,44], 7]
# print(a[2])

# a = {
#     1:1,
#     4:4,
#     'lius': {
#         'tree':3,
#         '4':43,
#         '5':5,
#         '7':7
#     }
# }
# print(tuple(a))
# print(a['lius']['tree'])

# from pprint import pprint
# users = {
#     '1234567890': {
#         'name': 'aktan',
#         'last_name': 'Kevirov',
#         'age': 20,
#     }
# }
# user = input("Введите ваш ИИН: ")
# name = input("Введите ваше имя: ")
# last_name = input("Введите вашу фамилию: ")
# age = input("Введите ваш возраст")
# d = users[user] = {
#         'name': name,
#         'last_name': last_name,
#         'age': age,
#     }
# pprint(d[user])


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in a:
#     if i <= 9:
#         continue
#     elif i >= 9:
#         print(i)
#     else:
#         print("Больше 10 нету")
  

# a = 54067
# b = str(a)
# for val in b:
#     if val == "0":
#         continue
#     print(val)
# print("The end")

# a = ['azamat', 'sultan', 'asan', 1, 3, 4, 5, 6, 78, 8, 9, 7, 3]
# for i in a:
    # if type(i) == str:
    #     print(i)
# print(a[1])

# a = ['aslan', 'sultan', 'baran', 'azamat', 'baizak', 0, 8, 9]
# b = []
# # a[3] = "aktan"
# # print(a)
# for i in a:
#     if type(i) == str:
#         continue
#     if i == 8:
#         i += 10
#         b.append(i)
#     else:
#         b.append(i)
# print(b)
        
# a.append(10)
# print(a)


# for i in range(1, 10):
    # c = 5
# print(f'{i} * 5 = {i*5}')
    

# a = []
# for i in range(0, 40):
#     if i * 
    


# тема modules.py
from pickle import TRUE
import random 
from random import random, randint,randrange,choice, shuffle
from time import sleep
from types import LambdaType

# print(random.random())
# print(random())
# print(randint(1, 10))
# print(randrange(0, 100, 5))

a = ['kani', 'aybarchyn', 'beks', 'argen', 'baiel']
# print(choice(a))
# print(a)
# shuffle(a)
# print(a)
# for i in a:
#     print(i)
#     sleep(1)

from datetime import datetime
# print(datetime.today().strftime('%d-%m-%y %H:%M:%S'))

# now = datetime.now()
# print(now)

# timeobj = time()

# start = datetime.now()
# for i in a:
#     print(i)

# end = datetime.now()
# print(end-start)

import os

# os.mkdir('hello')
# os.clear()

from string import ascii_letters

# print(ascii_letters)

# password = ''
# while len(password) <8:
#     L = choice(ascii_letters)
#     password += L

# while 


password = 'QWE'
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0

