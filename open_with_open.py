# file = open("text.txt",mode = "r",encoding='utf-8')
# print(file.read())
# file.close()
# file = open("text.txt",mode = "r",encoding="utf-8")
# for name in file:
#     if "Agil" in name:
#         print(name)
#     else:
#         print("no")


file =open("text.txt",mode = "r",encoding="utf-8")
for k,v in enumerate(file,1):
    print(k,v)

# file.close()

# file2 = open('new.txt',mode = "w",encoding="utf-8")
# file2.write("hello world\n")
# file2.write("привет мир\n")
# file2.write("good day")
# file2.close()

# file3 = open("new.txt",mode ="a",encoding="utf-8")
# file3.write("hello Agil")
# file3.write("!!!!")
# file3.close()

# login = input("введите свой логин:   ")
# password = input("введите свой пароль :   ")
# regis = open("name_pas.txt",mode="a",encoding="utf-8")
# regis.write("логин   " + login + "\n")
# regis.write("пароль   "+ password + "\n")
# regis.close()

# with open("ааа.txt", mode = "a",encoding="utf-8") as f:
#     f.write("как дела")




#1
# data='''additionlly      domachka.py     ifelif.py  list_tuple.py  open_with_open.py
# directories.txt  forandwhile.py  kosmos.py  open.txt    '''
# file = open("new.txt",mode="w",encoding= "utf - 8"  )
# file.write(data)

# file.close()

#2
# login = input("введите свой логин:   ")
# password = input("введите свой пароль :   ")
# regis = open("users.txt",mode="a",encoding="utf-8")
# regis.write("логин   " + login + "\n")
# regis.write("пароль   "+ password + "\n")
# regis.close()

#3
# a = ''' windows '''
# file = open("bbb.txt",mode = "w",encoding='utf-8')
# file.write(a)
# file.close()
# file = open("bbb.txt",mode = "r",encoding="utf-8")
# for name in file:
#     if "w" in name:
#         print("“Да, в тексте есть w”")
#     else:
#         print(" “Нет, в тексте нет w”")

#4
# # Classroom = '''   Python is a widely used high-level programming language for general-purpose
# # programming, created by Guido van Rossum and first released in 1991. An interpreted
# # language, Python has a design philosophy that emphasizes code readability (notably
# # using whitespace indentation to delimit code blocks rather than curly brackets or
# # keywords), and a syntax that allows programmers to express concepts in fewer lines of
# # code than might be used in languages such as C++ or Java.  '''
# # file = open("python.txt", mode="w", encoding="utf-8")
# # file.write(Classroom)
# # file.close()
# t_words = []
# with open('python.txt', mode='r') as f:
#     for file in f.read().split():
#         if "t" in file or "T" in file:            
#             t_words.append(file)
# print(t_words)

# 5
# a = '''"логин  "  umarchik02,ermek05, baitikk  "\n" '''
# b = '''"пароль " 46555551,465484515, 484512, umar5454  "\n" '''
# file = open("login.txt", mode="w", encoding="utf-8")
# c = a+b
# file.write(c)
# file.close
# v = input("войти или зарегистрироваться:  ")
# w = input("введите свой логин:   ")
# p = input("введите свой пароль :   ")
# with open("login.txt",mode="r",encoding="utf-8") as f:
#     for file in f.read().split():
#         if  w  in file:
#             print("уже  существует")
#         if p in file:
#             print("уже  существует")

# l = input("введите свой пароль:   ")
# p = input("повторите свой пароль :   ")  
# if l == p :
#         print("спасибо")
# elif l!=p:
#         print(" повторите пароль снова у не совпадают ")
#         s = input("введите свой пароль:   ")
#         k = input("повторите свой пароль :   ")
# regis = open("login.txt",mode="a",encoding="utf-8")

# regis.write("пароль   "+ p + "\n")
# regis.close()



# #6
# a = '''2, 5, 5,55'''
# file = open("b#6.txt", mode="w",encoding= "utf-8")
# file.write(a)
# # file = open("b#6.txt", mode="r",encoding= "utf-8")
# print( результат: min(a))
# file.close