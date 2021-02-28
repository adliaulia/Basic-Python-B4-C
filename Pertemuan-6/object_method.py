class data_diri:
    #constractor
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    
    #method / function
    def sapa(self):
        print("HALLO, Nama saya adalah "+self.nama)
        print("Dan umur saya", self.umur,"tahun")

p3 = data_diri("Adli",20)
# print("Nama saya saya adalah "+p3.nama)
# print("Umur saya adalah",p3.umur)
p3.sapa()