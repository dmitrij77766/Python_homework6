# Создайте список из случайных чисел. Найдите количество различных элементов в нем.

# import random
# n = int(input("Сколько элементов создать? "))
# list1 = []
# for i in range(n):
#     list1.append(random.randint(1, 10))
# print('Созданый список - ', list1)
# res = []
# for i in list1:
#     if i not in res:
#         res.append(i)
# print('Различных элементов - ', len(res))

# Пользователь вводит число K - количество фруктов. 
# Затем он вводит K фруктов в формате: название фрукта и его количество. 
# Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.

# listFruit = {}
# amount = int(input("Количество фруктов: "))
# for i in range(amount):
#         name = input("Название фрукта: ")
#         amountFruit = int(input("Количество: "))
#         listFruit[name] = amountFruit
    
# print(listFruit)


# Пользователь вводит число N. 
# Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.

# list1 = {}
# amount = int(input("Количество друзей: "))
# for i in range(amount):
#         name = input("Имя: ")
#         amountFriends = int(input("Возраст: "))
#         list1[name] = amountFriends
# print(list1)
# min_value = min(list1.values())
# for name, am in list1.items():
#         if am == min_value:
#             print('Самый младший - ', name)

# Пользователь вводит число N. 
# Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Выведите средний возраст всех друзей и самое длинное имя.

# a = int(input('Введите количество друзей:'))
# name = [] 
# age = 0  
# for i in range(a):  
#    q = input('Введите имя и возраст друга через пробел:').split()  
#    name.append(q[0])  
#    age = age + int(q[1])  
# age = age // a  
# print(age)
# print(max(name,key=len))

# 4. Английский словарь
# "Пора учить английский язык", - сказал себе Степа и решил написать программу для изучения английского языка. Программа получает на вход слово на английском языке и несколько его переводов на русском языке. Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов. В этой задаче нужно использовать строчный

words = {'apple': 'яблоко', 'orange':'оранжевый, рыжий ,апельсин', 'grape': 'виноград , виноградный, гроздь', 'easy': 'простой, легкий , нетрудный , удобный , несложный'}
for word in words:
 a = input('Введите слово на Англиском из списка(apple, orange, grape, easy):')
 print(word, ':', words[word].split(','))

  
