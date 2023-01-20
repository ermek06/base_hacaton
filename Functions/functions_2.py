# return
# def hello():
#     return "Agil where are you my love baby"
# # message = hello()
# print(hello())

# def sum(a,b):
#     return a +b
    
# print(sum(2,5))
# def square(x):
#     return x ** 2
# print(square(3))

# def get_max(a,b):
#     return a if a > b else b
# print(get_max(6,6))
# from math import *

# def cylinder():
#     r = float(input(":    "))
#     h = float(input(":    "))
#     side = 2 * pi * r * h
#     circle = pi * r**2
#     full = side + 2 * circle
#     return side,circle,full
# print(cylinder())

# def cylinder(r,h):
    
#     side = 2 * pi * r * h
#     circle = pi * r**2
#     full = side + 2 * circle
#     return side,circle,full
# print(cylinder(2.34,123.123))


# *args and **kwargs


# def name(*args):
#     for i in args:
#         return i
# word =("kak dela s funkciyami?")

# print(name(word))


# def find_animal(*args):
#     if "dog" in args:
#         return True
# print(find_animal("cat","mouse",12,32,False,"dog"))

# def infor(game, **kwargs):
#     players = []
#     numbers = []
#     if game =="football":
#         for k,w in kwargs.items():
#             players.append(k)
#             numbers.append(w)
#         return game,players,numbers
# print(infor(game = "football",alex = "first", bob = "second",messi = "ten",ronaldo = "seven"))

# def phone_book(**kwargs):
#     name = []
#     phone = []
#     for k,v in kwargs.items():
#         name.append(k)
#         phone.append(v)
#     return name,phone
# print(phone_book(agil = "+9969379992", egida = "+996love"))



# def add(x,y) :
#     return x-y
# print(add(5,8))
# def substract(x,y) :
#     return x+y
# print(add(5,8))
# def multiply (x,y) :
#     return x*y0.
# print(add(5,8))
# def divide(x,y) :
#     return x/y
# print(add(5,8))
# count = 0
# def my_list(a=str):
#     while
 #2
# message = input("строка")
# sum = 0

# def fffff():
#     global message
#     global sum
   
#     for i in message:
#         sum+=1
#     return sum
# print(fffff())
        
#3
# def dict(a,b):
#     a.update(b)
#     return a 
# a = {input("a: "): input("b: ")}
# b = {input("new: "): input("new2: ")}
# print(dict(a,b))

#4
# def menu():
  
#     file = open("menu.txt",mode = "w",encoding='utf-8')
   
#     file.write(input("че будешь кушать"))
#     file.write(input("drink"))
#     file.close()

# print(menu())

#5
# def solo(a):
    
#     file = open(a,mode = "w",encoding='utf-8')
#     file.write("welifjwljfkij'lfr'j")
# solo("ark.txt")
#1
# def camoro():
#     text = "Я главная функция"
#     print(text)
#     def cabrik():
#         text1 = "Я вложенная функция."
#         print(text1)
#     cabrik()
# camoro()




# 2
# def dict(a:dict):
#     c = []
#     w = []
#     for k,v in a.items():
#         c.append(k)
#         w.append(v)
#     return tuple(c),tuple(w)
# print(dict({'a':7}))     


# #3
# a = int(input("Введите число "))
# def camoro(a):
#     if a % a == 0 and a % 1 == 0:
#         return a
# print(camoro(a))    



#3.1

# def list1(a,b):
#     return list[a], list[b]
# print(list1(5,"sdhd"))

#3.2
a = input("Введите текс:  ")
def text(*agrsсв ):
    for i in len(a):
        a.split()
print(text())

#3.3
# def dodge(name, zp = 5000):
#     text = f'ИМЯ - {name}, Зарплата -  {zp} "'
#     print(text)
# dodge("jake", 5888)
# dodge('jake')

#3.4
# a = int(input("Введите число:   "))
# def camoro(*args):
#     return list[a]
# print(camoro())
