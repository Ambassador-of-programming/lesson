# a = ["Azamat", "Almaz", "John", "Bektur"]
# for i in a:
#     if i in "Almaz":
#         print("Да все отлично")
#         break
#     else:
#         print('такого слова нет')
#         break


# a = ['Azamat', 'Almaz', 'John', 'Bektur', 'Kanat', 'Bob', 'Akyl', 'Asel', 'Bermet', 'Sabina']
# for i in a:
#     if i == 'Almaz':
#         print('Da gudda')
#     else:
#         print('Takogo slova net')


# for i in range(1,10):
#     a = i * i
#     print(a)

# a = []
# b = int(input('Enter num:'))
# for i in range(b):
#     a.append(i)
# print(a)


# a = ['Azamat', 'Almaz', 'John', 'Bektur', 'Kanat', 'Bob', 'Akyl', 'Asel', 'Bermet', 'Sabina']

# a = [1,2,3,4,4,4,4,4,5,6,7,8,9]
# count = 0
# count = count + 8
# print(count)
# count = 0
# for i in a:
#     if i == 4:
#         count += 1
# print(count)
# for i in a:
#     if i == 4:
#         print(i)
# for i in range(1,10+1):
#     b = 5
#     c = b * i
#     print(f'{b} * {i} = {c}')


# b = int(input('VVedi chislo: '))
# a = ['Bishkek', 'Piter', 'Moscow', 'Naryn', 'Osh', 'Batken']
# for i in range(len(a)):
#     if b == i:
#         print(a[i])
  
# a = ['Bishkek', 'Piter', 'Moscow', 'Naryn', 'Osh', 'Batken']
# for i in a:
#     if i == 'Osh':
#         a.remove('Osh')
# print(a)

# i = 1
# while i < 50:
#     if i != 0:
#         i += 1
#     # i.reverse()
#     print(i)


# count = 0
# a = int(input('Enter num: '))
# while a !=0:
#     print('Repeat')
#     count += 1
#     a = int(input('Enter num: '))
# print(f'Вы потратили {count} попыток')

# a = [1,2,3]*5
# print(a)
# while 3 in a:
#     a.remove(3)
#     print(a)



# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)

# lst = ['Alice', 'Bob', 'Carl', 'Dave']
# x = 'Chris'
# i = 2
# lst[i] = x
# print(lst)


# for i in 'hello world':
#     print(i * 2, end='')


# for i in 'hello world':
#     if i =='w':
#         continue
#     print(i * 2, end='')


# a = 0
# while a < 5:
#     a +=1
#     if a == 3:
#         break
#     print(a)

# while True:
#     n = int(input('n='))

#     if len(str(n)) != 3:
#         print('No')
#     else:
#         print('Yes')
#         break

# b = 'hello world'
# for i in enumerate(b):
#     print(i)


# s = 0
# for i in range(1,6):
#     s += 1
#     print(s) 


# a = int(input('Введи количество цифр: '))
# for i in range(a+1):
#     print('*'*i)


# a = ['azamat', 'bektur', 'ilgiz', 'nikita', 'joma', 'arsen', 'Mars']
# b = int(input('Enter number: '))
# for i in range(len(a)):
#     if b == i:
#         print(a[i])


# guess = input('Введите пароль:')
# password = 'qwerty'
# count = 0
# while guess != password:
#     count +=1
#     print('Wrong password')
#     guess = input('Введите пароль: ')
# print(f'Вы потратили {count} попыток')

# a = ['azamat', 'bektur', 'ilgiz', 'nikita', 'joma', 'arsen']
# for i in a:
#     if i == 'nikita':
#         continue
#     print(i, end=', ')

# a = ['Bish', 'osh', 'batken','karakol', 'kant', 'naryn', 'talas']
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


# Problem 1
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']



# Problem 2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == "php":
#         print("остановлен на php")
#         print(i)
#         break


# Problem 3 
# a = 7
# b = 7
# for i in range(1,6):
#     i = a * b
#     print(i)

# Problem 4
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in enumerate(languages):
#     print(i)

# Problem 5
# a = []
# b = []
# for i in range(1, 10):
#     a.append(i)
#     b.append(i)
# b.reverse()
# a.extend(b)
# print()

# Problem 6
#  Если первое имя = 0, второе имя = 1 и т.д.
#  Выведите на экран всё имена которые лежат на чётных числах

# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in range(len(names)):
#     if i % 2 ==0:
#         print(names[i])
#     elif i % 1 == 0:
#         print(names[i])

# Problem 7
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in 