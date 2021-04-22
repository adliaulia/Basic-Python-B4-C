# print("Masukkan input!")
# nama = input("Masukkan Nama Anda: ")
# umur = int(input("Masukkan Umur Anda: "))
# tinggi=float(input("Masukkan Tinggi Anda: "))

# print("Nama saya "+nama+", umur saya {} tahun dan tinggi saya {} cm".format(umur, tinggi))

# print("Program Menghitung Luas Lingkaran")
# r = int(input("Masukkan jari jari: "))
# pi = 22/7
# luas = pi * r * r
# print(type(luas))
# print("Luas lingkaran dengan jari-jari {} cm adalah {} cm\u00b2".format(r, luas))

# #Bonus
# print("Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2".format(r, luas))

print("Nilai ujian praktik mahasiswa")
x = float(input("Masukkan nilai ujian teori: "))
y = float(input("Masukkan nilai ujian praktik: "))
if (x >= 70 and y >= 70):
    print("Selamat, anda lulus!")
elif(x >=70 and y < 70):
    print("Anda harus mengulang ujian praktek")
elif(x < 70 and y >= 70):
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktek")

