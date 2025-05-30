# 1
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(map(lambda x: x ** 2, n))
print(f'{n}\nSquare: {a}')

# 2
result = list(filter(lambda x: x % 2 == 0, n))
print(f"Even nums \n{result} from {n}")

# 3
strings = ['jinwooo', 'jinho', 'chha', 'kaizen', 'nezuko', 'zenizu']
result = list(map(lambda x: x.title(), strings))
result2 = list(map(lambda x: x.upper(), strings))
print(result)
print(result2)

# 4
new_n = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9]
result = list(filter(lambda x: x >= 0, new_n))
print(f' All positive numbers from the list consisting of negative n also!\n{result}')

# 5
result = list(filter(lambda x: len(x) > 5, strings))
print(f'Names consisting of more than 5 letters are {result}')

# 6
lens = list(map(lambda x: len(x), strings))
word = list(filter(lambda x: x > 5, lens))
print(f'Len of the words consisting of more than 5 letters!\n{word}')


# 7
result = list(filter(lambda x: x < 0, new_n))
print(f'All negative numbers from the list consisting of negative n also!\n{result}')

# 8
result = list(map(lambda x: x * 2, n))
print(f'Original list: {n}\nTimes two:{result}')

# 9
result = list(filter(lambda x: strings.index(x) % 2 == 0, strings))
print(f'Original list: {strings}\nElements with even indexes: {result}')

# 10
intstr = [1, 'i', 2, 'love', 3, 'you', 4]
result = list(filter(lambda x: type(x) == int, intstr))
print(f'Original list: {intstr}\nOnly nums: {result}')

