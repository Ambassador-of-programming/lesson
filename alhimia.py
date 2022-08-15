# bool = True          
# str = "ykctaulyifwoehPDHUYV;DOHI'B" !
# int =  6
# float = 5.6

# tuple = ('ASDSA', 'ASD', 524, 5.6)
# list = ['FSDFSF', '74955645', 787, 2345].append(4)
# set = {'asdad', 'aasd', 1, 1, 1, 1}
# dict1 = {
#     'key': {
#         'key1': 'value'
#     }
# }


# l = [[[[[[[],['value']]]]]]]


# print(dict1['key']['key1'])
# print(l[0][0])








# a = [True, True, True]


# print(all(a))


# a = [2,4,8,6,7,8,9,6,4,3]

# b = []
# for i  in a:
#     if i % 2 == 0:
#         b.append(True)
#     else:
#         b.append(False)

# print(all(b))




# a = [2,4,8,6,7,8,9,6,4,3]

# b = []
# for i  in a:
#     if i % 2 == 0:
#         b.append(True)
#     else:
#         b.append(False)

# print(any(b))
# print(abs(-500))


# a = [2,4,8,6,7,8,9,6,4,3]
# print(min(a))
# print(max(a))
# print(sum(a))



# a = [2,4,8,6,7,8,9,6,4,3]
# b = reversed(a)

# print(list(b))

# while True:
#     eval(input('>>>'))


# print(slice(a, 5, 2))


# a = 10/3

# print(round(a, 2))


# Problem 1


# Problem 2
# try:
#     set1 = set()
#     for i in range(5):
#         a = int(input("Введите число: "))
#         set1.add(a)
# except ValueError as y:
#     print(f'У вас такая вот ошибка {y}')
# except NameError as y:
#     print(f'У вас такая вот ошибка {y}')
# print(min(set1))


# Problem 4
# try:
# if user <= 50000:
#     user1 = []
#     print('Вы должны ввести сумму больше 50000 тысяч')
#     user = int(input("Введите сумму займа: "))
#     user = int(input("Введите сумму займа: "))
#     b = user / (3.47 * 100)
#     user1.append(b)
        
# else:
#     print('14r')# user.append(user1)
# print(user1)
# except ValueError :
#     print("Вводител только цифры")


# users = []
# while True:
#     user = int(input('Введите сумму займа: '))
#     if user > 50000:
#         b = user / (3.47 * 100)
#         c = round(b, 2)
#         users.append(c)
#         print(users)
#     else:
#         print('Vvedite zanovo')

# сумма разделенное на количество
# user = []
# while True:
#     user1 = input('Введите число: ')
#     if user1 == 'end':
#         break
#     user.append(int(user1))
# # summ = user + user

# print('your digits: ', ' '.join(str(i) for i in user))
# print('summ: ', sum(user))
# print('delenie: ', sum(user)/len(user))
    
    