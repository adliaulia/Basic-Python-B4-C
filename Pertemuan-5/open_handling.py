f = open("file.txt", "a")
a = input("Masukkan nama :")
f.write(a+"\n")
b = input("Masukkan nama :")
f.write(b+"\n")
f.close()

f = open("file.txt", "r")
# print(f.read())
data = []
for x in f:
    data.append(x)
f.close()

# print(data[0])
# print(data[1])