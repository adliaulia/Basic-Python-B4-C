print("Selamat datang!")
nama = input("Silakan masukkan nama anda : ")
umur = input("Silakan masukkan umur anda : ")

#cara pertama
print()
print("Nama Pelanggan : "+nama)
print("Umur Pelanggan : "+umur+" Tahun")

#cara kedua
int_umur = int(umur)
print()
print("Nama Pelanggan :",nama)
print("Umur Pelanggan : {} Tahun".format(int_umur))