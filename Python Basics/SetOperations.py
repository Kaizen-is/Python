# # 1
# nums = [1, 2, 5, 7, 4, 65, 4, 3, 6, 7, 3, 4, 6, 3, 4, 6]
# nSet = set(nums)
# print(nSet)
#
# # 2
# nSet.add(10)
# print(nSet)
#
# # 3
# nSet.remove(2)
# print(nSet)
#
# # 4
# nSet.discard(1909)  # We do not get an error
# print(nSet)
#
# #5
# popped = nSet.pop()
# print(popped)

#6
# import numpy as np
# lis1 = np.random.randint(10, size = 20).tolist()  # we are getting a python list not an array
# a = set(lis1)
# print(a)
# lis2 = np.random.randint(10, size = 6).tolist()
# b = set(lis2)
# print(b)
#
# union = a | b # 7
# print(union, ': Union')
#
# intersect = a & b  # 8
# print(intersect, ': Intersect')
#
# exception = a - b # difference  # 9
# exception2 = b - a
# print(exception2, ': Difference or except B ')
# print(exception, ': Difference or except A ')
#
# symmetric_difference = a ^ b     # 10
# print(symmetric_difference, ': Symmetric Difference')


# 11
# word = 'Kaizen'
# sSet = set(word)
# print(sSet)

# 12
# s = {1, 2, 3, 4, 5, 6}
# print(5 in s)
# print(1009 in s)
#
# #13
# s.update([404, 12, 100])
# print(s)


# 14
# def count_unique(x):
#     sset = set(x)
#     s = len(sset)
#     return f"Unique elements amount: {s}"
# print(count_unique(lis1))

#15
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# a = set(list1)
# b = set(list2)
#
# inter = a & b
# print(inter)




# String
# 1
# fruits = ["apple", "banana", "apple", "peach"]
# set_of_fruits = set(fruits)
# print(set_of_fruits)


# 2
# farben = ["rot", "grun"]
# farbset = set(farben)
# farbset.add("blau")
# print(farbset)


# 3
# fruits2 = ["apple", "banana", "peach"]
# fruitsSet = set(fruits2)
# fruitsSet.remove("banana")
# print(fruitsSet)


# 4
# a, b = {1, 2, 3}, {3, 4, 5}
# union_set = a | b # a.union(b)
# print(union_set)


# 5
# a, b = {"a", "b", "c"}, {"b", "c", "d"}
# intersected_set = a & b # a.intersection(b)
# print(intersected_set)


# 6
# a, b = {1, 2, 3, 4},  {3, 4, 5}
# except_set = a - b # a.difference(b)
# print(except_set)


# 7
# a, b = {1, 2, 3},  {3, 4, 5}
# symmetric_difference = a ^ b # a.symmetric_difference(b)
# print(symmetric_difference)


# 8
# klein = {2, 3}
# groB = {1, 2, 3, 4}
# print(klein in groB)
# print(klein.issubset(groB))
# #------------------
# list_a = list(klein)
# list_b = list(groB)
# result = []
# r = False
# for i in list_a:
#     if i in list_b:
#         result.append(i)
#         r = True
# print(f"{set(list_b)}: {set(result)}, {r}")


# 9
# klein = {"a", "b"}
# groB = {"a", "b", "c", "d"}
# print(klein in groB)
# print(klein.issubset(groB))
# #------------------
# list_a = list(klein)
# list_b = list(groB)
# result = []
# r = False
# for i in list_a:
#     if i in list_b:
#         result.append(i)
#         r = True
# print(f"{set(list_b)}: {set(result)}, {r}")


# 10
# x, y = {1, 3, 5}, {2, 4, 6}
# print(x.issubset(y))

# l_x = list(x)
# l_y = list(y)
# result = []
# b = False
# for i in l_x:
#     if i in l_y:
#         result.append(i)
# if result:
#     print(f"{result}: found in both")
# else:
#     print("There are no common elements")


# intersect = x & y
# if intersect:
#     print(f"{intersect}: found in both")
# else:
#     print("There are no common elements")


# 11
# print("""
#          1
#        1   1
#      1   2   1
#    1   3   3   1
#  1   4   6   4   1
#  """)
#
#
# len_r = 5
# t = []
# for x in range(len_r):
#     row = [1]
#     for y in range(1, x):
#         row.append(t[x-1][y-1] + t[x-1][y])
#
#     if x > 0:
#         row.append(1)
#     t.append(row)
#
# for row in t:
#     print(" ".join(map(str, row)).center(len_r * 4))


# 12
# n = int(input("n: "))
# for i in range(n - 1):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i + 1):
#         print("*", end= " ")
#     print()
#
# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for j in range(i, n - 1):
#         print("*", end=" ")
#     for j in range(i, n):
#         print("*", end= " ")
#     print()

# 13
# n = int(input("n: "))
# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for j in range(i, n - 1):
#         print("*", end=" ")
#     for j in range(i, n):
#         print("*", end= " ")
#     print()
#
#
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i + 1):
#         print("*", end= " ")
#     print()











