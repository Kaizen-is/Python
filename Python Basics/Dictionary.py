# # 1
# friends = {'name':'Kaizen', 'age':19, 'city':'Tokyo'}
#
# # 2
# print(friends['name'])
#
# # 3
# friends['country'] = 'Japan'
#
# # 4
# friends['age'] = friends['age'] + 5
# print(friends['age'])
#
# # 5
# del friends['city']
# print(friends)
#
# # 6
# # try:
# #     hobb = friends['hobby']
# #
# # except KeyError as k:
# #     print(f"There is an error related to the Key: {k}")
#
#
# # -----
# # popH = friends.pop('hobby')
# # print(popH)
#
#
# # 7
# print(friends.keys())
#
# # 8
# print(friends.values())
#
# # 9
# for k, v in friends.items():
#     print(f"Key:{k}, Value:{v}")
#
# # 10
# for k, v in list(friends.items()):
#     if k == 'country' and v == 'Japan':
#         friends['region'] = 'Central Asia'
# print(friends)
#
#
# # 11
# students = {'Kaizen':95, 'Cha Chein':88, 'Gojo':99, 'Zenizu':67, 'Jinho':43}
#
# # 12
# for k, v in students.items():
#     print(f"{k}'s score - {v}")
#
# # 13
# print('Students with highest scores!')
# for k, v in list(students.items()):
#     if v > 90:
#         print(f"{k}'s score - {v}")
#
# # 14
# print('Students who failed!')
# for k, v in list(students.items()):
#     if v < 60:
#         v = 'Fail'
#         print(f"{k}: {v}")
#
# # 15
# student = {'Student1':{'name':'Kaizen','age':16, 'major':'Computer Science'},
#            'Student2':{'name':'Cha Chein','age':23, 'major':'Cyber Security'},
#            'Student3':{'name':'Gojo','age':21, 'major':'Data Analytics'},
#            }
#
# # 16
# i = 0
# for k in student:
#     i = i + 1
# print(f'In the class - {i} students')
#
#
# # 17
# students = {'Kaizen':95, 'Cha Chein':88, 'Gojo':99, 'Zenizu':67, 'Jinho':43}
# score = []
# name = []
# for k, v in list(students.items()):
#     score.append(v)
#     name.append(k)
# score.sort()
#
# students2 = dict(zip(name, score))
# print(students2)
#
#
# # 18
# max_score = max(students.values())
# for k, v in list(students.items()):
#     if v == max_score:
#         print(f"The best student - {k}: {v}")
#
# # 19
# max_score = min(students.values())
# for k, v in list(students.items()):
#     if v == max_score:
#         print(f"The worst student - {k}: {v}")
#
# # 20
# new_score = {}
# for k, v in list(students.items()):
#     new_score[k] = v + (v / 100 * 10)
#
# print(new_score)


# 21
friends2 = {'Kaizen':['Kaizetse', 'Kaizetsu'],
            'Jinwoo':['Jinho'],
            'Eren':['Armin', 'Edren, Mikasa'],
            'Shin':['Makima'],
            'Zenizu':['Tanjiro', 'Keni', 'Shin', 'Takigama']}

# 22
#
# for k, v in friends2.items():
#     print(f"{k}'s friends are!")
#     for i in list(v):
#         print(i)
#     print("------------------------")
#
# # 23
# a = []
# for k, v in friends2.items():
#
#     lene = len(list(v))
#     a.append(lene)
# maximale = max(a)
#
#
# for k, v in friends2.items():
#     if len(v) == maximale:
#         print(f"{k} has max amount of friends:{maximale}")
#     for i in list(v):
#         print(i)


# 24
for k, v in friends2.items():
    if len(list(v)) >= 2:
        print(f"{k}: {v}")


# 25
country = {
    "Uzbekistan": ["Tashkent", "Samarkand", "Bukhara"],
    "Germany": ["Berlin", "Munich", "Hamburg"],
    "Japan": ["Tokyo", "Osaka", "Kyoto"]
}

# 26
for k, v in country.items():
    print(f"Country: {k}\nCities:")
    for i in list(v):
        print(i)
    print("--------------------")

# 27
newd = {}
for k, v in country.items():
    if k[0] == 'G':
        newd[k] = v
print(newd)


# 28
products = {
    "non": 30000,
    "sut": 90000,
    "yog'": 25000,
    "tuxum": 120000,
    "shakar": 150000
}
print("Products costing more than 50000!")
for k, v in products.items():
    if v > 50_000:
        print(f"{k}:{v}")


# 29
for k, v in products.items():
    if v < 30_000:
        print(f"For {k} you got a discount!")

# 30
sums = sum(products.values())
print(sums)











#--------------------------------------------------------------------


# Creating Dictionary
#from itertools import count

# 1
# fruits = {"banana":45_000, "apple":55_000, "watermelon":50_000, "cucumber":39_000}
# fruits.setdefault("peach", 88_000)
# print(fruits)
#
# # 2
# cities = dict(Tashkent = 36_000_000, France=42_000_000, India= 2_000_000_000, Dubai = 3_450_000)
# print(cities)
#
# # 3
# user = dict([("a", 1), ("b", 2)])
# print(user)
#
# # 4
# a = ["name", 'age']
# b = ['Alice', 25]
# users = dict(zip(a, b))
# print(users)
#
# # 5
# num = {x: x * x for x in range(1, 6)}
# print(num)

# zip()

# 1
# k = ["name", "age", "country", "email", "is_student"]
# v = ["Jinwoo", 16, "Uzbekistan", "jinwoo@example.com", True]
#
# privat = dict(zip(k, v))
# print(privat)
#
#
# # 2
# name = ['Kaizen', 'Jinwoo', 'Levi']
# age = [18, 24, 34]
# city = ['Tokyo', 'Pikin', 'Seul']
#
# user2 = list(zip(name, age, city))
# print(user2)
#
# # 3
# name, age, city = zip(*user2)
# name = list(name)
# age = list(age)
# city = list(city)
# print(name, age, city)
#
# # 4
# st = 'abc'
# lis= [1, 2, 3]
# print(dict(zip(st, lis)))

# get()

# 1
# print(fruits.get('banana'))
#
# # 2
# print(fruits.get("country", "unknown"))
#
# # 3
# for key in fruits:
#     print(fruits.get(key))
#
# # 4
# print(fruits.get("Jupiter"))
#
#
# # Adding Elements
#
# # 1
# fruits["Coconut"] = 46_000
# print(fruits)

# 2

# friends = {}
# i = 1
# print("Enter names and age of your 3 friends!")
# while i <= 3:
#     print(f"Friend {i}!")
#     n = input("name: ")
#     a = int(input("age: "))
#     friends[n] = a
#     i+=1
#
# print(friends)

# 3
# nested = {"a":1,
#           "b":{"a":2, "b":3}}
# n = {"c":3}
# n["g"] = nested
# print(n)


# Del()

# del fruits["banana"]
# print(fruits)


# for k in list(fruits):
#     if k[0] == 'a':
#         del fruits[k]
#
# print(fruits)


# pop()

# fruit = fruits.pop('banana')
# print(fruit)
# print(fruits)
#
#
# for k in list(fruits):
#     if k[0] == "w":
#         fruits.pop(k)
# print(fruits)


# popitem()

# anime = {'Jinwoo':'Solo Leveling', 'Nezuko':'Demon Slay', 'Levi':'Attack on Titan', 'Mike':'Tokyo Revengers'}
#
# last = anime.popitem()
# print(last)
#
# #
#
# del_anime = []
# anime3 = anime
# for k in list(anime):
#     anime = anime3.popitem()
#     del_anime.append(anime)
# print(del_anime)
# print(anime3)
#
# anime_dic = dict(del_anime)
# print(anime_dic)
#
# #
#
# # keys(), values(), items()
# anime = {'Jinwoo':'Solo Leveling', 'Nezuko':'Demon Slay',
#          'Levi':'Attack on Titan', 'Mike':'Tokyo Revengers'}
#
# print(anime.keys())
#
# print(anime.values())
#
# for k, v in anime.items():
#     print(f"{k}: {v}")

