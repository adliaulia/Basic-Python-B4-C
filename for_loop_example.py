name = []
age = []

while True:
    name.append(input("Masukan Nama Anda: "))
    age.append(input("Masukan Umur Anda: "))

    a = input("Apakah anda masih ingin menginput? (y/t): ")
    if a == "y":
        continue
    elif a == "t":
        for i in name:
            print("Nama: "+i) #name[i]
        for j in age:
            print("Umur: "+j+" Tahun") #age[j]
        exit()
    else:
        print("Pernyataan Salah, Coba Lagi.")  



