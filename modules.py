import random 
from random import random, randint, randrange, choice, shuffle
from time import sleep
from tracemalloc import start



# print(random.random())
# print(random())
# print(randint(1, 10))
# print(randrange(0, 100, 5))
# print(choice(a))
# shuffle(a)


# a = ['kani', 'aybarchyn', 'beks', 'argen', 'baiel', 'aktan', 'oxae', 'egdi', 'mars', 'nikiman', 'tilya']


# import time
# from time import sleep

# for u in a:
#     print(u)
#     sleep(1)


from datetime import datetime, time

# print(datetime.today().strftime('%d-%m-%y %H:%M:%S'))


# now = datetime.now()
# print(now)

# timeobj = time(8,1,45)
# timeobj2 = time(8,1,0)

# print(timeobj, timeobj2)

# start = datetime.now()

# for i in range(1, 1000000):
#     print(i)

# end =  datetime.now()

# print(end-start)





import os

# os.mkdir('hello')

# os.system('rm -rf hello')
# os.system('clear')

# os.system('mkdir hello')
# os.system('touch run.py')

from string import ascii_letters


# print(ascii_letters)




# while True:

#     password = ''
#     while len(password) < 8:
#         l = choice(ascii_letters)
#         password += l

#     print(password)
#     sleep(0.8)
#     os.system('clear')


# password = 'QWE'
# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# count = 0
# while True:
#     password1 = ''
#     while len(password1) < 3:
#         l = choice(letters)
#         password1 += l
#     if password1 == password:
#         count += 1444444
#         print(f'{password1} вы потратили {count} столько попыток')
#         break
# count = 0
# a = int(input('Enter num: '))
# while a !=0:
#     print('Repeat')
#     count += 1
#     a = int(input('Enter num: '))
# print(f'Вы потратили {count} попыток')
    