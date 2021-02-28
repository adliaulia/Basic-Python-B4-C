class person: #Superclass
    #constractor
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    
    #method / function
    def sapa(self):
        print("HALLO, Nama saya adalah "+self.nama)
        print("Dan umur saya", self.umur,"tahun")

class spesial_id(person): #Subclass
    #constractor
    def __init__(self,nama,umur,alamat,status):
        self.alamat = alamat
        self.status = status
        #penurunansifat
        person.__init__(self,nama,umur)
    def tampil(self):
        print(f"Nama anda adalah {self.nama}, umur anda adalah {self.umur} tahun, alamat anda adalah {self.alamat} dan status anda sekarang adalah {self.status} ")

while True:
    print("-- Menu --")
    print("1. Masukkan Data Diri Anda ")
    print("2. Tampilkan Biodata ")
    print("3. Keluar")
    pilih_menu = int(input("Pilih menu: "))

    if pilih_menu == 1:
        a = input("Masukkan nama anda: ")
        b = input("Masukkan umur anda: ")
        c = input("Masukkan alamat anda: ")
        d = input("Masukkan status anda: ")
        p1 = spesial_id(a,b,c,d)
    elif pilih_menu == 2:
        p1.tampil()
    elif pilih_menu == 3:
        print("Terima kasih, selamat tinggal!")
        exit()
    else:
        
        print("Tidak ada menu tersebut.")
        
