# 1)
# user = str(input("Enter your name!\n>>>"))
# print(f"Hello {user}!")

#2)
# print(len(user))
#
# #3
# print(user.upper())
#
# #4
# print(user.lower())
#
# #5
# print(user[::-1])

#
# name = reversed(user)
# rev_name = ''.join(name)
# print(rev_name)

#6
# print(user.count("a"))

#7
# txt = input("Enter any sized 2 texts!\n>>>")
# # txt2 = input(">>>")
# print(txt, txt2)

#8
# if user.title() == "Ali":
#     print("True")
# else:
#     print("False")

#9
# print(user.title())

#10
# if "python" in txt.lower():
#     print("True")
# else:
#     print("False")


#11
# print(user[:5])

#12
# print(user[-3:])


#13
# print(txt.replace(" ", ""))


# #14
# print(txt.replace(" ", "-"))


#15
# e = input("Enter your email!\n>>>")
# idx = e.index("@")
# i = int(idx)
# print(e[i + 1:])

#16
# num = input("Enter you number!\n>>>")
#
#
# for i in num:
#     if i.isalnum():
#         m = 0
#     else:
#         num = num.replace(i, "")
# print(int(num))

#17
# w = input("Enter any word\n>>>")
# for i in w:
#     print(i)

#18
# if w == w[::-1]:
#     print("Palindrom")
# else:
#     print("Not Polindrom")
#
#
# a = 0
# i = 0
# d = -1
# if len(w) % 2 == 0:
#     while i < len(w):
#         if w[i] == w[d]:
#             a = 1
#         else:
#             a = 2
#         i+=1
#         d-=1
#     if a == 1:
#         print("Palindrom")
#     else:
#         print("Not Polindrom")
#
# else:
#     num = len(w) - 1
#     num = num/2
#     num = int(num)
#     while i < len(w):
#         if w[:num - 1] == w[-num:]:
#             a = 1
#         else:
#             a = 2
#         i += 1
#     if a == 1:
#         print("Palindrom")
#     else:
#         print("Not Polindrom")


#19
# i = 0
# if "i" in w:
#     b = w.count("i")
#     i += b
# if "e" in w:
#     b = w.count("e")
#     i += b
# if "a" in w:
#     b = w.count("a")
#     i += b
# if "o" in w:
#     b = w.count("o")
#     i += b
# if "u" in w:
#     b = w.count("u")
#     i += b
# print(i)
#
#
# i = 0
# unli = "uioea"
# for l in unli:
#     i += w.count(l)
# print(i)


#20
# import pandas as pd
# import numpy as np
# l = len(w)
#
# lis = []
# for i in w:
#     lis.append(i)
# inde = pd.Series(lis, index = np.arange(0, l))
# inde.index.name = "index"
# inde.name = "Letters"
# print(inde) # вазифани чунмадим именно канака клиб индекс ни чикарищни, наппавй пандай окиганман



#1
# fruits = ['bananas', 'grapes', 'apple']
# fruits.append("New Fruit")
# print(fruits)
#
#2
# fruits.remove("New Fruit")
# print(fruits)
#
#3
# print(fruits[2]) # 0, 1 , 2 - 2 element
# print(fruits[1]) # 0, 1 - 2 element
#
#4
# print(fruits)
#
#5
# print(len(fruits))

#6
# length = []
# for i in fruits:
#     length.append(len(i))
# m = max(length)
# for i in fruits:
#     if len(i) == m:
#         print(f"The longest letter consisting word!\n{i}: {m}")
#
#7
# for i in fruits:
#     if i.lower() == "pear":
#         print("We got pear!")
#
# #-------
#
# if "pear" in fruits:
#     print("We got pear!")

#8
# fruits.sort()
# print(fruits)


#9
# fruits.sort(reverse=True)
# print(fruits)

#10
# print("Length")
# for i in fruits:
#     print(f"\n{i}: {len(i)}")

#11
# for i in fruits:
#     print(f"Fruit: {i}")

#12

# for i in fruits:
#     if "a" in i:
#         print(f"The word {i} contains {i.count("a")} 'a' letters!")


#13
# fou = []
# i = 0
# print("Enter fruits one by one!")
# while i <=  2:
#     user = input(">")
#     fou.append(user)
#     i+=1
# print(fou)
# fruits2 = fou
#
# #14
# if fou[0] == fou[1]:
#     print(f"{fou[0]} and {fou[1]} are equal!")
# elif fou[2] == fou[1]:
#     print(f"{fou[2]} and {fou[1]} are equal!")
# elif fou[0] == fou[2]:
#     print(f"{fou[0]} and {fou[2]} are equal!")
# else:
#     print("No same fruits")


#15
# fruits.extend(fruits2)
# print(fruits)

#16
# st = ""
# for i in fruits:
#     st += i
# print(st, sep = ",")
#
# print(",".join(fruits))
#
#17
# import random as rm
# ran = rm.randint(0, 2)
# print(fruits[ran])
#
#18
# fruit = fruits[1:3]
# print(len(fruit))
# print(fruit)
#
#19
# fruits.clear()
# print(fruits)




#1
array = ["apple", "banana", "peach", "grape"]
# for i in array:
#     print(i)

#2
# for i in array:
#     print(f"{i}: {len(i)}")

#3
# for i in array:
#     print(i.title())

#4
# for i in array:
#     print(i[::-1])

#5
# import numpy as np
# ar = np.arange(1, 11)
# for i in ar:
#     print(i ** 2)

#6
# for i in ar:
#     print(i * 2)

#7
name = ["Kira", "Kaizen", "IzzKoo", "Eren", "Yamada", "Ayumi"]
# for i in name:
#     print(f"Helo, {i}")

#8
# t = input("Enter any sized txt!\n>")
# for i in t:
#     print(i)

#9
# userF = []
# i = 1
# print("Enter names of your five friends!")
# while i <= 5:
#     user = input(">>")
#     userF.append(user)
#     i+=1
# print(userF)
# for i in userF:
#     print(i)


#10
# e = 0
# new = []
# for i in name:
#     if i[e][0].lower() == "a":
#         new.append(i)
#         print(f"{i}: 'a'")
#         e +=1
# print(new)


#11
# e = 0
# count = 0
# for i in name:
#     if "e" in i:
#         count +=1
#         print(f"{i}:  {count}")
#     e +=1

#12
# a = 0
# u = input("Word: ")
# letter = "ieuoa"
# for l in u:
#     if l in letter:
#         a +=1
# print(f"{u}: {a}")
#
#
# a = 0
# letter = "uioea"
# for l in letter:
#     a += u.count(l)
# print(a)

#13
e = 0
li = list(range(len(name)))
for i in name:
    print(f"{i.ljust(7)} -  {li[e]}")
    e+=1