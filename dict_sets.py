# empty_dict = {}

# dict1 = {
#     1:2,
#     'str': 'string',
#     'bool': True,
#     'list': [1,2,3],

# }

# person = {
#     'name': 'John Smith',
#     'age': 30,
#     'profession': 'Python dev'
# }


# person['height'] = 180
# person['age'] = 40
# person['planet'] = 'earth'
# person2 = {'race': 'ork'}
# person.update(person2)
# person.pop('age')# удаляет по ключу
# c = person.get('race')
# print(c)
# print(person)
# print(person['name'])
# person.clear()# очищает словарь
# a = person.copy()# копирует словарь
# person.setdefault(7, 'seven')#Создает новую пару ключ-значение,но если такой ключ уже есть, ничего не произойдет
# print(person.values())
# print(person.keys())
# print(person.items())

# dict_1 = {}
# dict_1['one'] = 1
# print(dict_1)

# aa = person.keys()
# bb = person.values()
# cc = person.items()
# print(cc)
# print(len(person))

# for key in person.keys():
#     print(key)

# for values in person.values():
#     print(values)

# for key, value in person.items():
#     print(f'{key} = {value}')

# for key in person:
#     if key == 'name':
#         person['name'] = 'Will SMith'
#     elif key == 'age':
#         person['age'] +=8
# print(person)


# a = set()
# b = 10
# c = '12'
# d = True
# a.add(b)#добавляет элемент в множество
# a.add(c)
# a.add(d)
# print(a)

# set_1 = {1,2,3,4,4,4,4,4,4,5,6,7,8}
# print(set_1)
# set_1.clear()#очищает множество
# print(set_1)


# set1 = {'arsen','almaz','bob', 'john', 'beka', 'mars'}# показывает недостающие элементы / разницу множеств
# set2 = {'arsen','almaz','bob', 'abay', 'manas', 'iosif'}
# set3 = set2.difference(set1)
# print(set3)

# a = {1,2,3}
# b = {4,5,6}
# a.update(b)#добавляет одно множество в другое
# a.remove(1)#удаляет элемент из множества
# print(a)


# a = {1,2,3,4,5}
# b = {1,2,3,7,8,9}
# c = a.intersection(b)# Выводит одинаковые данные из множеств
# print(c)


# a = {
#     'number':[4,7,8]
# }

# for value in a.values():
#     print(value[0])

# Problem Zero
# dates_of_birth = {3,10,11,13,31,21,10,3,5,6,6}
# dates_of_birth.add(7)
# dates_of_birth.remove(7)
# print(dates_of_birth)

# Problem 1
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Suriname']
# south_american_countries1 = ['Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# c = set(south_american_countries)
# c1 = set(south_american_countries1)
# d = c.intersection(c1)
# print(d)

# Problem 2
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# d = farm_1.difference(farm_2)
# print(d)

# Problem 3
# mnogo = {1,2,3,4,5}
# mnogo.add(6)
# mnogo.pop()
# print(mnogo)

# Problem 000
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# besh = {'besh_barmak': 130}
# menu.update(besh)
# menu['lagman']= 135
# menu.pop("borsh")
# print(menu)

# Problem 10
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu["drinks"] = ["Coca cola", "Sprite", "Fanta"]
# print(menu)

# Problem 020

# Problem 31
# slovar = {}
# for i in range(1):
#     b = input("Введите ваше имя: ")
#     slovar[b] = d = input("введите пароль: ")
# print(slovar)

# a = []
# for i in range(1):
#     b = input('введиетк ')
#     a.append(b)
# print(a)

# Problem 27
# users = {"Ambak": "cooker",
#         "Aida": "medik",
#         "Beka": "programmer"}
# for key, walue in users.items():
#     print(f"Имя: {key}, профессия: {walue}")

# users = {
#     'Admin':{
#         'name':'admin',
#         'phone':'996555444333',
#         'balance':'500',
#         'password':'12312321'
#     },
#     'Argen':{
#         'name':'Argen',
#         'phone':'0999580780',
#         'balance':'500',
#         'password':'12312321'
#     }
# }
# key = None
# while True:
#     if key is None:
#         print('Здраствуйте уважаемый клиент!')
#         m = int(input('''
#         1 Заарегистрироваться 
#         2 Авторизоваться 
#         3 Перевод баланса
#         4 Список пользователей 
#         5 Информатция 
#         6 Выход из банка
#         >>> '''))
#         if m == 1:
#             login = input('введите логин ')
#             name = input('введите полное ваше имя ')
#             phone = int(input('введите ваш номер +996'))
#             password = input('Придумайте пароль ')
#             password1 = input('Подтвердите пароль ')
#             while password != password1 and len(password) < 8:
#                 password = input('Ваш паролль не совподает или она меньше 8 символов \n>>>')
#                 password1 = input('Повторите пароль ')
#             else:
#                 users.update((
#                     login : (
#                         "name" : name,
#                         "phone" : phone,
#                         "balance" : 100,
#                         "password" : password
#                     )
#                 ))
#                 print("Регистрация успешна")
#                 key = login
#             if a == 2:
#                 if key is None:
#                     print("Добро пожаловать в авторизацию")
#                     login = input("Введите логин")
#                     password = input("Введите пароль")
#                     if login in users:
#                         if password == users(login)("password"):
#                             print("Вы авторизовались")
#                             key = login
#                         else:
#                             print("Не верный пароль")
#                         else:
#                             print("Нет такого пользователя")


# dicts = {"Abulak": 500, "Faloc": 50, "Igor": 35, "Gari": 220}
# print(f"Список пользователей{dicts}и их денег на счету")
# while True:
#     command = input('''Выберите действие:
#     > Добавить
#     > Отобразить 
#     > Удалить
#     > Выход
#     >''')
#     if command == "Добавить":
#         add = input("Добавьте пользователя")
#         summa = int(input('vvedite summu '))
#         dict.update({
            
#         })
# print(dicts)


# d = {
#     1:3,
#     "true": True,
#     "list": [1,2,4],
#     "name": ("Bob Marley": "+77 555 999",
#     "Nicky Romero": +996555333766)
# }

# print(d("name"))

# a = {"11":"33"}
# b = {1,2,2,3,4}
# print(type(b))

