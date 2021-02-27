data = open("database.txt", "a")
print("Selamat Datang!")
name = input("Masukkan Nama: ")
data.write(name+"\n")
phone = input("Masukkan No. Telepon: ")
data.write(phone+"\n")
print("Data Berhasil Ditambahkan!")
data.close()

read = open("database.txt", "r")
data = read.readlines()
for x in range(0,len(data),2):
    print("Nama\t\t: {}\nNo.Telepon\t: {}".format(data[x],data[x+1]))
read.close()