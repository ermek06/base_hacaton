# import os
# # print(os.name) # название операционной системе
# # print(os.getlogin())
# print(os.uname())


# import csv
# with open('students.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["ID", "Name", "Duration"])
#     writer.writerow([1, 'Aktan', 'Python'])
#     writer.writerow([2, 'Dima', 'JS'])
#     writer.writerow([3, 'Amal', 'Flutter'])

    #  module OS.
# import os
# # print(os.name) Назавание операционной системы
# # print(os.getlogin()) # имя пользователя операционной системы
# print(os.uname()) # информация оперционной системы

# модуль Sys Модуль sys обеспечивает доступ к некоторым переменным и
#  функциям, взаимодействующим с интерпретатором python.
# import sys
# print(sys.platform) оперционна система

# print(sys.argv) путь в котором вы на
# # ходитесь
# print(sys.version) # версия пайтона


# from datetime import *
# import time


# print(datetime.now()) показывают действующее время
# print(datetime.today())
# a = datetime(2023,1,13,19,1,13) задается полная да от года до секунды(по вашему усмотрению)
# print(a)
# b = time(11,34,56)задается нужное вам время
# print(b)
# c = time(hour = 11,minute=33,second=12) детально выводим время
# print(c)

# print("Agil")
# time.sleep(5) задержка времени на 5 сек
# print("hello")

# for i in range(5):
#     print("Agil pomolchi po bratski")
#     time.sleep(3) задержка в три секунды для вывода строки  5 раз 
# d = date(2023,1,13)
# print(d) задается дата

# inform = datetime(2023,1,13,19,14)
# print("year=",inform.year)  вытаскиевает по значениям 
# print("month=",inform.month)
# print("hour=",inform.hour)
# print("hour=",inform.minute)

# from datetime import *

# now = datetime.now()
# t = now.strftime("%H:%M:%S") формат сокращкния по часу, минутам и секундам
# print("time:", t)


# s = now.strftime("%A,%Y,%m,%d") сокращение по недели, году, месяцу и дню

# print(s)


# import random


# my_list = ["agil","banan","apple","Egida"]
# random.shuffle(my_list) перемешивает список
# print(my_list)
# print(random.choice(my_list)) достает случайный элемент из списка

# print(random.randint(1,50)) диапозон от 1 до 50, случное число вытаскивает
# print(random.randrange(0,10,2))

# print(random.random())# рандомное число до одного

# import urllib.request модуль для открытия Url адресов

# a = urllib.request.urlopen("https://www.itcbootcamp.com/#/")
# print(a.read()) считывается html код страницы
# print(a.getcode()) код доступа 200, что значит сайт подходит для получения информации


# Простейший пример записи CSV файла:
# import csv
# with open('students.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["ID", "Name", "Duration"])
#     writer.writerow([1, 'Aktan', 'Python'])
#     writer.writerow([2, 'Dima', 'JS'])
#     writer.writerow([3, 'Amal', 'Flutter'])

# #1
# from  modulis import a
# a






#2
# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# print(random.sample(names, 4))


#3
# import os
# print(os.name)


#5

# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# a = len(names)//4
# print(a)
# print(random.sample(names,a))
# print(random.sample(names,a))
# print(random.sample(names, a))
# print(random.sample(names,a))





import sys
a = input("Введите значение:  ")
b = input("Введите еще одно значение:  ")
print(sys.getsizeof([a,b]))