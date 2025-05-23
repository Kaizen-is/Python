# # 1
# def greet(name):
#     print(f'Hello, {name}!')
# greet('Kaizen')
#
# # 2
# def square(n):
#     print(f'Square of {n} is {n * n}')
# square(100)
#
# # 3
# def add(a, b):
#     print(f'Sum of {a} and {b} is {a + b}')
# add(10, 4)
#
# # 4
# def even(num):
#     if num % 2 == 0:
#         print(True)
#     else:
#         print(False)
# even(2)
#
# # 5
# def say_hello():
#     print('Hello, world!')
# say_hello()
#
# # 6
# def d_list(list1):
#     new = []
#     for i in list1:
#         new.append(i + 2)
#     return new
# print(d_list([1, 2, 3, 4, 5, 6, 7]))
#
# # 7
# def first(text):
#     return text[0]
# print(first('Jinwoo'))
#
# # 8
# def time(a, b):
#     return f'{a} * {b} = {a * b}'
# print(time(3, 4))
#
# # 9
# def circle(r):
#     return 3.14 * (r**2)
# print(circle(3))
#
# # 10
# def welcome(name, age):
#     return f'Welcome {name}!.You are {age} right?'
#
# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# print(welcome(name, age))

# 11
def vowels(txt):
    n = 0
    for i in txt:
        if i in ['a', 'o', 'u', 'e', 'i']:
            n += 1

    return f'{n} vowels in this word'
print(vowels('Hello')) # 2 vowels


# 12
def reverse(txt):
     return ''.join(reversed(txt))
print(reverse('Hello'))


# 13
def palin(txt):
    rev = ''.join(reversed(txt))
    if rev.lower() == txt:
        return True
    else:
        return False
print(palin('kauaki'))

# 14
nums = [21, 32, 45, 53, 62, 76, 8, 45, 67, 23, 45, 62, 12, 34, 54]
def max_num(num):
    return f'{max(num)} is max element in \n{num}'
print(max_num(nums))

# 15
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(3))

# 16
def remove(lis):
    new = set(lis)
    return list(new)
print(remove([1, 2, 1, 3, 4, 2, 3]))

# 17
def count_words(txt):
    n = 0
    txt = txt.title()
    for i in txt:
        if i.isupper():
            n += 1
    return n
print(count_words('one, two three four five six seven'))

# 18
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a = b
        b = a + b


# 19
# def prime(num):
#     i = 1
#     while i <= 2:
#         if num == 1:
#             return '1 is not a prime number!'
#         prim = True
#         n = 2
#         while n <= num ** 0.5:
#             if num % n == 0:
#                 prim = False
#                 break
#             n += 1
#         if prim == True:
#             return 'Prime'
#         else:
#             return 'Not Prime num'
#     i += 1
# print(prime(7))

# 20
# def length(words):
#     new = {}
#     for i in words:
#         v = len(i)
#         new[i] = v
#     return new
#
# print(length(['apple', 'banana', 'peach', 'cat', 'dog']))


def length(words):
    new = {}
    n = []
    for i in words:
        n.append(i)
        v = len(i)
        new[v] = n
        n = []
    return new

print(length(['banana', 'peach', 'cat']))