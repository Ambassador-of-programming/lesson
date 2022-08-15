# print('hello')
# range()
# len('hello')
# sum([1,2,4,6])

# def print_asan():
#     print('hello')
#     print('world')
#     print('asan')



# print_asan()
# print_asan()
# print_asan()

# print(print_asan())




# a = [1,2,4,5,6,7,64,3,3,2,4,5,6,6]
# b = [1,2,4,5,6,7,64,3,3,2,4,5,6,6]

# def my_len():
#     s = 0
#     for i in a:
#         s += 1
#     print(s)


# def my_len(l):
#     s = 0
#     for i in l:
#         s += 1
#     return s



# print(len(a))
# print(my_len())


# a = [1,2,4,5,6,7,64,3,3,2,4,5,6,6]
# b = [1,2,4,5,6,3,4,5,7,64,3,3,2,4,5,6,6]


# print(my_len(a))
# print(my_len(b))




# def my_sum(a, b, d):
#     return a + b + d

# s = my_sum(6, 56, 9)

# print(s)


# Problem 1

# a = list_1[:2]
# a.reverse()
# b = list_1[2:]
# b.reverse()
# list_2.extend(a)
# list_2.extend(b)
# print(list_2)



# list_1 = ['name', 'age', '1', '19', 'sdf', 'dfgh']
# def my_perevorot(a):
#     list_2 = []
#     mid = len(a) // 2
#     ret1 = list_1[:mid]
#     ret2 = list_1[mid:]
#     ret1.reverse()
#     ret2.reverse()
#     list_2.extend(ret1)
#     list_2.extend(ret2)
#     return list_2
# print(my_perevorot(list_1))


# def gen_number():
#     from random import choice
#     num = '0444'
#     for x in range(6): #Количество символов (16)
#         num += choice('145790')
#     return num

# for i in range(1, 10):
#     print(i, f'Ваш номер телефона {gen_number()}')


# def kvdrat(x, n=2):
#     return x ** n


# print(kvdrat(9))


# def login(name, age=18):
    # return f'Ваше имя = {name}, Ваш возраст = {age}'

# print(login('Kiri', 19))




# def func(*args):
#     for i in args:
#         if i % 2 ==0:
#             return i
#     print('hello')

# print(func(1,3,4,5,6,7,87,4))


# def func(**kwargs):
    # return kwargs

# print(func(name='aktan', age=17))


# def chet_necheat(x):
#     if x % 2 ==0:
#         return f' {x} Четное'
#     else:
#         return f' {x} Нечетное'

# for i in range(10):
#     # print(chet_necheat(i+1))

# def chetnoe(x):
#     if x % 2 ==0:
#         return True
#     return False

# print(chetnoe(9))


# for i in range(1,20):
#     if chetnoe(i):
#         print(i, 'четное') 
#     else:
#         print(i, 'нечетное')


# Problem 1
# def add(x, n):
#     return x + n
# def substarct(x, n):
#     return x - n
# def muiltiplay(x, n):
#     return x * n
# def divide(x, n):
#     return x / n
# print(add(2,5))
# print(substarct(5, 3))
# print(muiltiplay(10, 5))
# print(divide(14, 7))


# Problem 2
# a = [1,2,4,5,6,7,64,3,3,2,4,5,6,6]
# def my_len(l):
#     s = 0
#     for i in l:
#         s += 1
#     return s
# print(my_len(a))


# Problem 3

# aktan = {'name': 'aktan'}
# akylai = {'name': 'akylai'}

# def my_dict(x, a):
#     x.update(a)
#     return x
# print(my_dict(aktan, akylai))


# Problem 4
# eda = input('Что хотите кушать: ')
# vipit = input('Что хотите выпить: ')
# def zakaz(x, a):
#     with open('user.txt', 'a') as file:
#         file.write(f'Название еды: {x} ')
#         file.write(f'Название напитка: {a}')
# zakaz(eda, vipit)

# with open('user.txt', 'r') as f:
#     s = f.read()
#     print(s)


# Problem 5
# import os
# os.system('touch aktan.py')


# a = []
# for i in range(2, 100):
#     k = 0
#     for j in range(2, i):
#         if i % j == 0:
#             k += 1
#     if k == 0:
#         a.append(i)
# print(a)


# Problem 6
# def max_f(x):
#     def min_f(x):
#         return f'Маленькая фукнция {x}'
#     print(min_f(x))

# max_f('Большая функция')

# Problem 
# al = []
# def my_ot():
#     x = input('Введите ваш имя: ')
#     y = input('Введите вашу зарплату: ')
#     al.append(f'ваше имя: {x}')
#     al.append(f'ваша зарплата: {y}')
#     return al
# print(my_ot())


from .def2 import my_funct

print(3**3,4**1)