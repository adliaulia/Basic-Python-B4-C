#Membuat program yang dapat menyimpan nama dan kontak
list_kontak = []

def menu():
    print()
    print("Selamat datang!")
    print("-- Menu --")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

def daftar_kontak():
    for item in list_kontak:
        print("Nama: {}".format(item["nama"]))
        print("No. Telepon: {}".format(item["telepon"]))

def tambah_kontak():
    nama = str(input("Nama: "))
    telepon = int(input("No. Telepon: "))
    list_kontak.append({'nama':nama,'telepon':telepon})
    print("Kontak berhasil ditambahkan")

def keluar():
    print("Program selesai, sampai jumpa!")
    exit()

while True:
    menu()
    input_menu = int(input("Pilih menu: "))
    if input_menu == 1:
        daftar_kontak()
    elif input_menu == 2:
        tambah_kontak()
    elif input_menu == 3:
        keluar()
    else:
        print("Menu tidak tersedia")