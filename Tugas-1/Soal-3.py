print("Selamat datang! ")
ujian_teori = float(input("Masukkan Nilai Ujian Teori Anda : "))
ujian_prak = float(input("Masukkan Nilai Ujian Praktek Anda : "))

if ujian_teori >= 70 and ujian_prak >= 70:
    print("Selamat, anda lulus!")
elif ujian_teori >= 70 and ujian_prak < 70:
    print("Anda harus mengulang ujian praktek.")
elif ujian_teori < 70 and ujian_prak >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")