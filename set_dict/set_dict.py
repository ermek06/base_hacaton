# dates_of_birth = {3,10,11,13,31,21,7,1,10,3,5,6,6}
# dates_of_birth.remove(7)
# print(dates_of_birth)


#  farm_1 = {"dog", "cat", "mouse", "sheep"}

#  farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
#  farm_1.intersection(farm_2)
#  print(farm_1)


# farm_1 = {"dog", "cat", "mouse", "sheep"}

# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_1.intersection_update(farm_2)
# print(farm_1)

# a = {1,2,2,89,8}
# a.add("hello")
# a.pop()
# print(a)

# menu = {"borch": 100, "bech_barmak": 130, "kacha":  85}
# menu["bech_barmak"]= 135
# menu.pop("borch")
# print(menu)

# menu = {"borch": 100, "bech_barmak": 130, "kacha":  85}
# a = {"Coca-Cola": 75, "Sprite": 77, "Fanta": 74}
# menu.update(a)
# print(menu)

# a = {"add", "update", "remove", "pop", "clear","discart", "intersection", "intersection_update", "difference" }
# b = {"clear", "ged", "keys", "values", "items", "update"}
# c = a.intersection(b)
# print(c)

person = {
    "user1":{
        "name":"ageil",
        "age": 18,
        "adress":["bishkek","baitik str."],
        "hobby":{"python":"junior","math":"professional"}
    },
    "user2":{
        "name":"arsen",
        "age": 12,
        "adress":["bishkek","12mkr. 52 dom"],
        "hobby":{"python":"junior","football":"play"}


    },
    
}
print(person["user1"]["adress"][1], person["user2"]["hobby"]["math"])

