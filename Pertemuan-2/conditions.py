#condition ==, != , >, <, >=, <=, and, or, not
a = 4
b = 5

if a>b:
    print("a lebih besar dari b")
elif a<b:
    print("a kurang dari b")
else:
    print("a tidak masuk semua kondisi")

c = 4
d = 5
if c == d:
    print("c tidak sama dengan d")
elif c != d:
    print("c tidak sama dengan d")
else :
    print("tidak masuk semua kondisi")

e = 5
f = 3
if e == 5 or f == 5:
    print("e atau f sama dengan 5")
else:
    print("e atau f tidak sama dengan 5")

g = 4
if not g == 4:
    print("g bukan 4")
else:
    print("g itu 4")
