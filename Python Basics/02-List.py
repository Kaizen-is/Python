# --------------------------------------------------------------------------
# 1

eine_liste = list(range(5, 51, 5))
print(eine_liste)

# # --------------------------------------------------------------------------
# # 2

products = ["apfel", "banane", "apfel shorle", "brot"]
products.append(["karotte", "gurke", "butter"])
print(products)


product= ["apfel", "banane", "apfel shorle", "brot"]
product.append("karotte")
product.append("gurke")
product.append("butter")
print(product)

# ---------------------------------------------------------------------------
menu = ["Oatmeal with fruit", "Grilled chicken salad", "Baked salmon with rice",
    "Scrambled eggs & toast", "Turkey sandwich", "Spaghetti with meatballs"]

print(f"Here is our menu!\nYou can make an order!\n{menu}")

customer = []

i = True
while i == True:
     order = str(input(">>>"))
     if order in menu:
         print("Order accepted!\nAny thing else?(Yes/No)")
         customer.append(order)
         answer = str(input(">>>"))
         if answer.title() == "Yes":
             print("What else?")
         else:
             print("Got it")
             break
     else:
         print("We do not have this food in the menu!")
print(f"Here is your order, {customer}")


# --------------------------------------------------------------------------
# 3

price = [12000, 25000, 19000, 31000, 40000]
print(max(price))
print(min(price))

# --------------------------------------------------------------------------
# 4
#
students = []
students.insert(0, "Zafar") # first place among and elements
students.insert(1, "Lola") # second
print(students)

students = []
students.insert(1, "Zafar") # first place among indexes
students.insert(2, "Lola")
print(students)

# --------------------------------------------------------------------------
# 5

num = [100, 200, 300, 400, 500]
del num[2]
print(num)

# --------------------------------------------------------------------------
# 6

num = [5, 10, 15, 20, 25, 30, 35]
newn = num.pop(-1)

print(newn)

# # --------------------------------------------------------------------------
# 7
n = [1, 2, 3, 4, 5, 6, 7]
print(n[2:5])

# --------------------------------------------------------------------------
# 8

numbers = [100, 200, 300]
num = numbers.copy()
num.append(400)
print(num)

# --------------------------------------------------------------------------
# 9

num = [1000, 2000, 3000]
num.clear()
print(num)

# --------------------------------------------------------------------------
# 10

a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

# --------------------------------------------------------------------------
# 11

mevalar = ['olma', 'shaftoli', 'o‘rik', 'nok']
print(mevalar[-1])

# --------------------------------------------------------------------------
# 12

cars = ['bmw', 'audi', 'tesla', 'kia']
cars.reverse()
print(cars)

# --------------------------------------------------------------------------
# 13

nums = [100, 150, 200, 250]
print(sum(nums))

# --------------------------------------------------------------------------
# 14

numbers = [5, 10, 15, 20]
number = sorted(numbers, reverse = True)
print(number)

# --------------------------------------------------------------------------
# 15

num = (10, 20, 30, 40, 50)
print(num[1:4])