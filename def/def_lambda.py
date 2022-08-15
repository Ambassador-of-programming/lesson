# sum_org = lambda a: a**2
# print(sum_org(44))

# s = (lambda a, b: a + b)(5,7)
# print(s)

# a = [4,7,9,9,3,6,8]
# for i in a:
#     print(i**2)

# for i in range(len(a)):
#     a[i]=(lambda x:x**2 )(a[i])
# print(a)

# s = map((lambda i:i**3), a)
# print(list(s))

# def even_or_odd(number):
#     if type(number) == int:
#         return 'Even'
#     if type(number) == float:
#         return 'Odd'
    
# print(even_or_odd(1.4))

# def even_or_odd(number):
#     if number % 2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'
# print(even_or_odd(2))

# a = [3, 2, 5, 6, 7, 33]
# def maps(a):
#     for i in range(len(a)):
#         a[i]=a[i]*2
#     return a
# print(maps(a))

# def simple_multiplication(number):
#     if number % 2 == 0:
#         return number * 8 
#     else:
#         return number * 9
# print(simple_multiplication(10))


# def are_you_playing_banjo(name):
#     if name.startswith('R') or name.startswith('r'):
#         return(f'{name} plays banjo')
#     else:
#         return(f'{name} does not play banjo')
# print(are_you_playing_banjo('Rafael'))

# def repeat_str(repeat, string):
#     return string * repeat
# print(repeat_str(10, 'aktan'))

#     return f'{string*repat}'
# print(repeat_str(10,'dog'))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# def count_positives_sum_negatives(a):
#     if len(a) == 0:
#         return []
#     cointer = 0
#     cointer1 = 0
#     for i in a:
#         if i > 0:
#             cointer += 1
#         if i < 0:
#             cointer1 += i 
#     return [cointer, cointer1]
# print(count_positives_sum_negatives(a))


# def find_needle(haystack):
#     s = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
#     index = s.index('needle')
#     return f'found the {s[5]} at position {index}'
# print(find_needle('needle'))


# s = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
# index = s.index('needle')
# print(index, s[5])

# def remove_char(b):
#     res_str = b[]
#     return res_str
# print(remove_char('aktan'))

# def abbrev_name(name):
#     name = name.upper().split()
#     name = (name[0][0]+"."+name[1][0])
#     return name
# print(abbrev_name('aktan imankulov'))

# def summation(num):
#     b = 0
#     for i in range(num+1):
#         b += i
#     return b

# def validate_pin(pin):
#     if len(pin) == 4 and  pin.isdigit() or len(pin) == 6 and  pin.isdigit():
#         return True
#     else:
#         return False
# print(validate_pin('1.42345'))

