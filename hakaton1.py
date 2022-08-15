# from random import choice

# students = ['Каный', 'Бексултан', 'Айбарчын', 'Тилек', 'Арген',
# 'Байзак', 'Актан', 'Эгида', 'Байэл', 'Нурдоолот', 'Эскен']

# team1 = []
# team2 = []

# while len(team1) !=6:
#     name = choice(students)
#   if name not in team1:
#     team1.append(name)

# while len(team2) != 5:
#     name = choice(students)
#   if name not in team1 and name not in team2:
#     team2.append(name)
    
# print('Команда 1', team1)    
# print('Команда 2', team2)


# Task 1 

# Problem 1
# print("Ноль в качестве знака операции"
#       "\nзавершит работу программы")
# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")



# Problem 2 
# a = [1, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
# a.append(13)
# if len(a) != len(s):
#     t = len(a) - len(s)
#     print('Значения встречаются', t)
# s = len(a)
# print(s, "длина списка")

# Problem 3
# users = []
# print("Добро пожаловать на регистрацию!!! ")
# name = input("Введите ваш логин: ")
# password = input("Введите ваш пароль: ")
# while len(password) <= 6:
#     password = input("Пароль не может быть меньше 6: ")
# users.append((name, password))
# # print(users)
# print("Пройдите авторизацию")
# name1 = input("Введите логин: ")
# password2 = input("Введите пароль: ")
# if name == name1:
#     print("\nВы успешно авторизовались!\n")
# else:
#     print("\nВы ввели ошибку!\n")

# Task 2 
# Problem 1
# dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# for i in dict1:
#     if dict1[i] % 3 == 0:
#         print("hi")
#     else:
#         print()
#     if dict1[i] % 5 == 0:
#         print("Bye")
#     else:()


# Problem 2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i, item in enumerate(languages):
#     print(i + 1, item)

# Problem 6
# words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
# if words == words:
#     print(words)



# Final
# a = []
# while True:
#     command = input('''Выберите действие: 
#     > Добавить 
#     > Отобразить
#     > Заменить 
#     > Удалить 
#     > Выход
#     > ''')
#     if command == 'добавить':
#         add = input('Добавьте новый город: ')
#         if add not in a:
#             a.append(add)
#             print('Город успешно добавлен')
#         else:
#             print('Такой город уже есть')
#     elif command == 'отобразить':
#         print(', '.join(a))
#     elif command == 'удалить':
#         print(', '.join(a))
#         rem = input('Выберите город для удаления:')
#         if rem not in a:
            
#             print('Такого города нет')
#         else:
#             a.remove(rem)
#             print('Город успешно удален')
#     elif command == 'выход':
#         break

#     elif command == 'заменить':
#         print(', '.join(a))
#         replace = input('Выберите город для замены: ')
#         replace2 = input('Введите название города: ')
#         if replace  in a:
#             a.remove(replace)
#             a.append(replace2)
#         else:
#             print('Такого города нет')