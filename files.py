# 'a' - аппендит в файл данные
# 'w' - перезаписывает файл полностью
# 'r - читает файл
# 'rb' - читает медию(картинки и.т.д)
#ls -R > all.txt запись всех файлов  в текст
# file = open('data/foto.jpg', 'rb')
# # file.write('Bishkek')
# print(file.read())


# file.close()


# a = ['Beka', 'Asyl', 'alan', 'rick', 'john', 'bob']
# file = open('names.txt', 'a')
# for i in a:
#     file.write(i)

# file.close()


# with open('text.txt', 'r') as f:
#     print(f.read())


# a = 'Hello world \n'
# with open('text.txt', 'w') as f:
#     f.write(a)


# with open('login.txt', 'a') as file:
#     login = input('Enter your login: ')
#     file.write('Логин: ')
#     file.write(login)
#     file.write('\n')
# print('Успешно создан файл с логином')



# names = ['Beka', 'Asyl', 'alan', 'rick', 'john', 'bob']
# with open('names.txt', 'w') as f:
#     for i in names:
#         f.write('\n')
#         f.write(str(names.index(i)))
#         f.write(' ')
#         f.write(i)
# print("Всё ок")

# a = 'Здесь должен быть какой то текст с какой нибудь инфой'
# with open('text2.txt', 'r') as f:
#     # f.write(a)
#     print(f.read().split())



# with open('n.txt', 'w') as f:
#     for i in range(10):
#         b = int(input('Введи число: '))
#         f.write(f'{b},')
# print('Файл успешно записан')


# a = 'home/lessons/data/f'

# with open('img', 'w') as f:
#     f.write('data/foto.jpg')

# b = '../Изображения/linux.png'
# with open('tt.txt', 'w') as f:
#     f.write(b)


# Problem 2
# user = input("Введите ваш логин: ")
# password = input("Введите ваш пароль: ")
# with open('user.txt', 'a') as f:
#     f.write(f"ваш логин: {user}")
# with open('user.txt', 'a') as f:
#     f.write(f"ваш пароль: {password}")
