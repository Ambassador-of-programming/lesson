# else - иначе
# if 2 - 1:
#     print ('hello world')

# a = 90
# if a % 2 == 0:
#     print('без остатка')

# age  = int(input ('введите ваш возраст'))
# if age >= 18:
#     print('вы можете зайти в клуб')

# elif age < 18 and age > 12:
#     print('ты еще ребенок и тебе нельзя войти в клуб')

# else:
#     print('ты еще ребенок')


# Problem 1
# a = 3**2
# b = 2**3
# if a > b:
#     print ('a > b')
# elif a < b:
#     print ('a < b')
# else:
#     print ('a == b')


# У нас есть числа от 0 до 100, но не все числа разрешены!
# Разрешенённые:
# От 0 до 21
# От 57 до 100
# Как узнать что какое-то число из запрещёного диапазона?
# Problem 2
# a = int(input('vvedite chislo ot 1 do 100: '))
# if a > 0 and a <=21:
#     print (a,'true')
# elif a > 57 and a < 100:
#     print ('от 57   до 100 разрешенные')
# else:
#     print(a,'False')


# Написать программу которая проверит число на несколько критериев:
# Чётное ли число?
# Делится ли число на 3 без остатка?
# Если возвести его в квадрат, больше ли оно 1000?
## Problem 3
# user = int(input ('введите число'))
# if user % 2==0:
#     print('вы ввели четное число')
# else:
#     print('вы ввели не четное число')


# Создайте условие которое будет срабатывать в любом случае
# Problem 4


# Problem 5
# a = 10//5
# b = 10/5
# if a == b:
#     print("их переменные равны")
# else:
#     print('их переменные не равны')

# print("переменная а ровна:",10//5)
# print("переменная b ровна", 10/5)

# Problem 6
# user = int(input("введите число"))
# if user < 0:
#     print("это отрицательное число")
# else:
#     print("это положительное число")

# Problem 7
# a = 10
# b = 5
# if a and b > 0:
#     print("положительное число")
# else:
#     print("нету положительных чисел")

# Problem 8
# if a >= b:
#     print("а2")
# else:
#     print("b2")

# Problem 9
# user = int(input("write here number"))
# if user > 0:
#     print("положительное число")
# elif user < 0:
#     print("отрицательное число")
# else:
#     print(user)

# Problem 10
# user = int(input("write your age: "))
# if user > 18:
#     print("вы соверншолетний")
# elif user > 4 and  user< 18:
#     print ("вы не соверншолетний")
# elif user <= 4:
#     print("ты ребенок")


# Problem 11
# a = 45
# b = 6
# if a / b:
#     print("данное значение делится")

# Problem 12
# user = int(input("Введите дату рождения: "))
# print (2022 - user)
# if 2022 - user > 18:
#     print("вы совершолетний")
# elif 2022 - user < 4:
#     print ("вы Ребенок")
# else:
#     print("вы не совершолетний")

# Problem 14
# a = 55
# b = 10
# d = 15
# if a > b and a > d:
#     print(a)
# elif b > d and a > b:
#     print(b)
# elif d > b and d > b:
#     print (d)
# if a < b and a < d:
#     print(a, 'меньше всех')
# if a > b and a > d:
#     print(a)
# elif b > d and a > b:
#     print(b)
# elif d > b and d > b:
#     print (d)

# Problem 15
# a = 17391 % 17
# b = 546 % 17
# d = 934 % 17
# if a < b:
#     print("остаток в a меньше всего")
# elif b < d:
#     print("остаток в b меньше всего")
# elif d < a:
#     print("остаток в d меньше всего")


# print (34 / 10)  #обычное деление
# print (34 % 10)  #деление по модулю показывает остаток

# name = input("введите ваше имя: ")
# text = f"Здравствуйте {name}, Вас приветствует ваш код!!!"
# print(text)

# if name.startswith ("A"):
#     print("Ваше имя начинается на А")
# else:
#     print("ваше имя НЕ начинается на А")

# text = "май, мир, труд"
# print (text.title()) # делает слова заглавными
# print (text.strip()) # удаляет пробелы
# s = "/" .join(text)
# print (s)
# print(text.count("м"))
# print (text.isalpha())
# print (text.isdigit())

# password =  input("Введите ваш пароль: ")
# if password.isalpha() or password.isdigit():
#     print("ваш пароль должен состоятьи и из букв и из цифр")
# elif len(password) < 8:
#     print("ваш пароль должен состоять длинее 8 цифр")
# else:
#     print("пароль подходит !")

# text = "hellt"
# print (text.replace("t", "o"))


# Problem 0
# text = "hello"
# text2 = "world"
# print (text.upper() + "" + text2.lower())

# Problem 1
# a = True
# print(str(a))

# Problem 2
# user = str(input("введите символ: "))
# user1 = '/'.join(user)
# a = "GitHub"
# b = '/'.join(a)
# print(user1 + b)


# Problem 3
# world = "Самые важные собЫтия в миРе инфосека за сентябрь"
# print (world.replace("е", "3"))

# Problem 4
# user_name = str(input("введите ваше имя: "))
# print(("Привет,"), user_name)
# user_film = str(input("введите ваш любимый фильм: "))
# print(("Ваш любимый фильм,"), user_film)

# Problem 5
# world = "Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем"
# print (len(world))

# Problem 6
# stroka = "Самые важные собЫтия в миРе инфосека за сентябрь"
# s = '/'.join(stroka)
# print (s)

# Problem 7
# slowo = "хакеры слили в сеть данные пакистанской энергетической компании k-Electric"
# print (slowo.title())

# a = " это число"
# b = 44
# print(str(44) + a)

# print("Добро пожаловать на регистрацию")
# login = input("Введите логин: ")
# password = input("Введите пароль: ")


