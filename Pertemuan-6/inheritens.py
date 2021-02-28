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
        print(self.nama)
        print(self.umur)
        print(self.alamat)
        print(self.status)

print("-- Menu --")
print("1. Masukkan Data Diri Anda ")
print("2. Tampilkan Biodata ")
pilih_menu = int(input("Pilih menu: "))

if pilih_menu == 1:
    a = input("Masukkan nama anda: ")
    b = input("Masukkan umur anda: ")
    c = input("Masukkan alamat anda: ")
    c = input("Masukkan status anda: ")
    p1 = spesial_id(a,b,c,d)
elif pilih_menu == 2 :
    print(f"Nama anda adalah {self.nama}, umur anda adalah {self.umur}, alamat anda adalah {self.alamat} dan status anda sekarang adalah{self.status} ")
