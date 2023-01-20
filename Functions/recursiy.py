#1
# aaa = lambda a,b,c: a*b*c
# a = "Объем бассейна:  "
# print(a,aaa(2,3,4))

# #2
# c = lambda a: a-19

# print("до нового года осталось ",c(365), " дней")



# def summma(nur):
#     def dodge(i):
#        print("нечетное")
#        nur()
#        return dodge
def num(a=list):
    ne = []
    ch = []
    for i in a:
        if i % 2 == 0:
            ch.append(i)
        else:
            ne.append(i)
    return ne
print(num(a=[1,2,5,3,2,5,2,7,3,5,7,9,5,23,342]))

num(1)         








# def fun_decorator(func):  #параметр Func ссылка на некую функцию
#     def wrapper():
#         print("яячто то делаю до вызова")
        
#         print("яя что то делаю после вызова ")
#         func()
#     return wrapper


# def some_func():
#     print("вызов функции")

# f =fun_decorator(some_func)
# f()