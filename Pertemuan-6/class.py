#cetakan
class Myclass:
    x = 5
    y = 10
class person:
    nama = 'Adli'
    umur = "22"
class data_diri:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
#pada fungsi, x tidak dapat dipanggil keluar jika tidak ada return
def luas(p,l):
    luas = p*l
    return luas

#object
p1 = Myclass() #class perlu didefinisikan terlebih dahulu jika ingin dipanggil
p2 = person()
p3 = data_diri("Adli",20)
print(p1.x)
print(luas(p1.x,p1.y))
print("Nama saya saya adalah "+p2.nama)
print("Umur saya adalah",p2.umur)
print("Nama saya saya adalah "+p3.nama)
print("Umur saya adalah",p3.umur)
