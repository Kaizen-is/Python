# # 1
# alex = {'name':'Ali', 'age':25}
#
# # 2
# name = input('Enter your name!\n>>')
# age = int(input('Enter your age!\n>>'))
#
# user = {'name':name, 'age':age}
# print(user)
# # ------------------------------- The task is not exactly defined
# alex = {'name':'Ali', 'age':25}
# alex['name'] = name
# alex['age'] = age
# print(alex)
#
# # 3
# print(user['name'])
#
# # 4
# alex['city'] = 'Tokyo'
#
# # 5
# alex['age'] = 26
# print(alex)
#
# # 6
# if 'age' in alex:
#     print('Key age exists in alex dict!')
# else:
#     print('Key age does not exists in alex dict!')
#
# # 7
# print(alex.keys())
#
# # 8
# print(alex.values())
#
# # 9
# a = alex.get('country', 'Not found')
# print(a)
#
# # 10
# for k, v in alex.items():
#     print(k, v)
#
#
# # 11
# del alex
# # clear alex
#
# # 12
# users = {'country':'Japan', 'major':'Data Analytics'}
# print(user | users)

# 13
# nums = {'a':10, 'b':20, 'c':30}
# maxed = max(list(nums.values()))
# for k, v in nums.items():
#     if v == maxed:
#         print(f"{k} has max num: {v}")
# # 14
# nums = {'a':10, 'b':25, 'c':50}
# for k, v in nums.items():
#     if v > 30:
#         print(f'More than 30\n{k}: {v}')
#     else:
#         print('No number is bigger than 30!')
#
# # 15
# key = []
# value = []
# onlys = {'a':1, 'b':'hello', 'c':3, 'd':'bye'}
# for k, v in onlys.items():
#     if v == str(v):
#         key.append(k)
#         value.append(v)
# string = dict(zip(key, value))
# print(string)
#
# # 16
# keys = ['a', 'b']
# values = [1, 2]
# print(dict(zip(keys, values)))
#
# # 17
# nums = {'a':5, 'b':10}
# for k, v in nums.items():
#     nums[k] = v * 2
# print(nums)
#
# # 18
# d = {"name": "Jinwoo", "age": "16", "country": "Uzbekistan",
#      "email": "jinwoo@example.com", "status": "student"
# }
# lened = []
#
# for k, v in list(d.items()):
#     l = len(list(v))
#     lened.append(l)
# m = max(lened)
#
# for k, v in d.items():
#     if len(v) == m:
#         print(f'Max letter consisting word: {k} - {v}({m})')
#
#
# # 19
# sums = []
# cou = 0
# for k, v in nums.items():
#     sums.append(v)
#     cou += 1
#
#
# print(sum(sums) / cou)
#
# # 20
# me = {'name':'kaizen', 'city':'tokyo', 'country':'japan'}
#
# capital = []
# key = []
# for k, v in me.items():
#     capital.append(v.title())
#     key.append(k)
#
# print(dict(zip(key, capital)))
#
# # 21
# student = {'student':{'name':'Kaizen', 'age':21}}
# print(student['student']['age'])
#
# # 22
# student['student']['age'] = 23
# print(student['student']['age'])
#
# # 23
# ld = [{'name':'Kaizen'}, {'name':'Jinwoo'}]
# print(f'Student1 {ld[0]['name']} \nStudent2 {ld[1]['name']}')
#
# # 24
# users = {1:{'name':'Kaizen', 'age':21},   # task is not exactly defined
#          2:{'name':'Jinwoo', 'age':1000},
#          3:{'name':'Nezuko', 'age':18}}
# print(users[1]['name'])
#
# # 25
# students = {
#     "student1": "A",
#     "student2": "B",
#     "student3": "A",
#     "student4": "C",
#     "student5": "B",
#     "student6": "A",
#     "student7": "C",
#     "student8": "B"
# }
# student = []
# keys = []
# for k, v in students.items():
#     student.append(v)
#     keys.append(k)
# students_set = set(student)
# print(students_set)
#
# counter_A = 0
# counter_B = 0
# counter_C = 0
# b = list(students_set)[0]
# a = list(students_set)[1]
# c = list(students_set)[2]
#
# for i in students.values():
#     if b == i:
#         counter_B += 1
#     elif a == i:
#         counter_A += 1
#     elif c == i:
#         counter_C += 1
#
# for i in list(students_set):
#     if i == a:
#         print(f'({i}) was counted: {counter_A} times!')
#     elif i == b:
#         print(f'({i}) was counted: {counter_B} times!')
#     elif i == c:
#         print(f'({i}) was counted: {counter_C} times!')
#
# # ---------------------------------------
# count_numbers = {}
#
# for value in students.values():
#     if value in count_numbers:
#         count_numbers[value] += 1
#     else:
#         count_numbers[value] = 1
# for key, value in count_numbers.items():
#     print(f'{key} was counted: {value} times!')
#
# # 26
# numerical = {"a": 42,"b": 7,"c": 89,"d": 16,"e": 73,"f": 58,"g": 31}

# key = []
# val = []
# for k, v in numerical.items():
#     key.append(k)
#     val.append(v)
# val.sort()
#
# i = 0
# for k, v in numerical.items():
#     if v == val[i]:
#         print(k, v)
#     i += 1

# 27

# word = (','.join(input("Enter any word!\n>>>").lower())).split(',')
# new_dic = {}
# n =0
# while n < len(word):
#     if word[n] in new_dic:
#         new_dic[word[n]] += 1
#     else:
#         new_dic[word[n]] = 1
#     n += 1
# print(new_dic)

# 28
# n = 1
# user_dic = {}
# print('Enter 5 keys and 5 values!')
# while n < 6:
#     k = input(f'Enter key number {n}:')
#     if k in user_dic:
#         print("You have already entered this key!")
#         continue
#     else:
#         v = input(f'Enter value number {n}:')
#         user_dic[k] = v
#     n += 1
# print(user_dic)


# 29
# students = {
#     "student1": "A",
#     "student2": "B",
#     "student3": "A",
#     "student4": "C",
#     "student5": "B",
#     "student6": "A",
#     "student7": "C",
#     "student8": "A"
# }
# counted = {}
# for v in students.values():
#     if v in counted:
#         counted[v] += 1
#     else:
#         counted[v] = 1
#
# values = []
# for k, v in counted.items():
#     values.append(v)
# m = max(values)
# for k, v in counted.items():
#     if m == v:
#         print(k, v)


# 30
i = 1
while i < 6:
    print(i)
    i += 1

# 31

# while True:
#     a = input("Enter any values: ")
#     if a.lower() == 'stop':
#         print("Stopped!")
#         break

# 32
# word = 'Hello my friend!'
# n = 1
# while n < 11:
#     print(word)
#     n += 1
#
# # 33
# n = 1
# timest = 1
# print(timest)
# while n < 10:
#     a = timest * 2
#     print(a)
#     timest = a
#     n += 1

# 34
n = 1
while n < 101:
    if n % 2 == 1:
        print(n)
    n += 1

# 35
# n = int(input("n: "))
# i = 1
# var = 0
# while n >= i:
#     var += n
#     n -= 1
# print(var)

# 36
n = 10
while n >= 1:
    print(n)
    n -= 1

# # 37
# print("This program will sum all the nums you enter, 0 breaks the program!")
# n = 0
# while True:
#     use = int(input('n: '))
#     if use == 0:
#         break
#     else:
#         n += use
# print(n)

# 38
# n = 1
# while n < 6:
#     star = '*' * (2 * n - 1)
#     space = ' ' * (5 - n)
#     print(space + star)
#     n += 1
#
# 39
# n = int(input('n!: '))
# a = 1
# while n >= 1:
#     a *= n
#     n -= 1
# print(a)

# 40
# corpass = 12345
# while True:
#     user = int(input('Please enter the password!'))
#     if user == corpass:
#         print('Correct')
#         break
#     else:
#         print('Error')


# 41
# import random
# a = random.randint(1, 10)
# while True:
#     user = int(input("num: "))
#     if user == a:
#         print('Correct', a)
#         break

# 42
# lis = []
# even = []
# while len(even) != 5:
#     user = int(input("n: "))
#     if user % 2 == 1:
#         lis.append(user)
#     else:
#         even.append(user)

# 43
# print('What is the value of P in degree?\n(you got 3 chances)')
# i = 1
# while i < 4:
#     user = float(input('P: '))
#     if user == 3.14:
#         print('Correct!')
#         break
#     else:
#         print(f'You got {4 - i - 1} attempt left!')
#     i += 1

# 44
# print('Enter letters!')
# n = ['a', 'b', 'c']
# us = []
# while True:
#     for i in range(1, 4):
#         u = input(f'Letter {i}:')
#         us.append(u)
#     if us == n:
#         print('Correct!')
#         break
#     else:
#         print('Try again!')
#     us = []

# 45
# while True:
#     user = input('Enter only nums!: ')
#     if user.isdigit():
#         print('Executed!')
#         break
#     else:
#         print('Error')
#
# # 46
# i = 0
# while True:
#     user = int(input(':'))
#     if user > 0:
#         i +=user
#     else:
#         break
# print(i)

# 47
# from random import randint
# i = 0
# a = []
# while i <= 10:
#     rand = randint(1, 100)
#     a.append(rand)
#     i += 1
# print(a)
# print(min(a))
#
# # 48
# nums = [1, 2, 5, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6, 7, 8]
# n = 0
# a = []
# while n < len(nums):
#     if nums[n] > 0:
#         a.append(nums[n])
#     n += 1
# print(a)

# 49
# i = 1
# result = []
# print('Enter 3 letters!')
# while i < 4:
#     user = input(':')
#     if user in 'aouie':
#         result.append(user)
#     i += 1
# print(result)

# 50
# while True:
#     num = int(input("Enter any num: "))
#     if num < 2:
#         print('Numbers being smaller than 2 are not prime nums')
#         continue
#     prime = True
#     n = 2
#     while n <= num ** 0.5:
#         if num % n == 0:
#             prime = False
#             break
#         n += 1
#     if prime:
#         print("Correct prime num !")
#         break
#     else:
#         print("This num is not prime, try again!")

# 51
# print('Enter password containing 8 characters!')
# while True:
#     user = input(':')
#     if len(user) >= 8:
#         print('Accepted!')
#         break
#     print("Password must contain at least 8 characters!")

# 52
# print('Enter your login!')
# log = '1234'
# i = 1
# while i < 4:
#     user = input(':')
#     if user != log:
#         print(f'You got {4 - i - 1} attempts left!')
#     else:
#         print('Accepted!')
#         break
#     i += 1
# if i ==4:
#     print('Blocked')

# 53
# i am using just letters instead of loong names
# emp = ['a', 'b', 'c', 'd']
# i = 1
# while i < 4:
#     user = input(f'users name {i}: ')
#     if user in emp:
#         print(f'({user}) Exist!')
#         continue
#     else:
#         emp.append(user)
#     i += 1
# print(emp)

# 54
# print('Guess random letter!')
# import random as r
# rand = r.randint(1, 10)
# while 1:
#     user = int(input(':'))
#     if user == rand:
#         print(f'Correct! ({rand})')
#         break
#     else:
#         print('Try again!')

# 55
# nums = 1000
# i = 1
# while i <= nums:
#     print(((i - nums) + nums) ** 2)
#     i += 1
#
# # 56
#
# text = (" ".join(input("Enter any sized text: ").lower())).split()
# new_dict = {}
# n = 0
# while len(text) > n:
#     if text[n] in new_dict:
#         new_dict[text[n]] += 1
#     else:
#         new_dict[text[n]] = 1
#     n += 1
# max_value = max(value for value in new_dict.values())
# for key, value in new_dict.items():
#     if max_value == value:
#         print(f"The most repeated key is {key}: {value} times")
#
# 57
# rand = [21, 32, 45, 53, 62, 76, 8, 45, 67, 23, 45, 62, 12, 34, 54]
# i = 0
# new = []
# while i < len(rand):
#     if rand[i] % 3 == 0:
#         new.append(rand[i])
#     i += 1
# print(rand)
# print(set(new))

# 58
# number = (" ".join(input("num: "))).split()
# n = len(number) - 1
# while 0 <= n:
#     print(int(number[n]), end='')
#     n -= 1

# 59





# 60
chars = ['*', '/', '-', '+']

while True:
    firt_num = int(input("Enter first num: "))
    second_num = int(input("Enter second num: "))
    print("Characters:", chars)
    a = input("Chose one of them: ")

    if a in chars:
        if a == '+':
            res = firt_num + second_num
        elif a == '-':
            res = firt_num - second_num
        elif a == '*':
            res = firt_num * second_num
        elif a == '/':
            if second_num == 0:
                print('Can not equal to 0')
                continue
            res = firt_num / second_num
        print(f"{firt_num} {a} {second_num} = {res}")
    else:
        print("Unsupported character")
        continue
    b = input("q - used to exit! ").lower()
    if b == 'q':
        break


