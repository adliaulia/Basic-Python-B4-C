#Membuat program untuk menghitung luas lingkaran
pi = 22/7
print("Selamat datang! Berikut ini dapat menghitung luas lingkaran.")
r = int(input("Masukkan nilai jari-jari lingkaran : "))

luas_lingkaran = pi*(r**2)
print("Luas lingkaran dengan jari-jari {} cm adalah {} cm\u00b2.".format(r,luas_lingkaran))

#Bonus: Ubah format luas menjadi 2 angka dibelakang koma
print("Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2.".format(r,luas_lingkaran))