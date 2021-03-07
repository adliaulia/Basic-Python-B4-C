#dictionary data tdk terurut, dapat diubah, dan memiliki index
dict = {"brand":"Ford","model":"Mustang","year":1964}
print(dict)

for x in dict:
    print(x)

#change value
dict["year"] = 2021
print(dict)

x = dict["year"]
print(x)