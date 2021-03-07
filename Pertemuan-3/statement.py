nilai =[100,70,30,40,70]
for i in nilai: #0 1 2 3 4 
    if i == 30:
        continue #dapat digunakan untuk memilah
    print("#1. Nilai {} = Lulus".format(i))

for i in range(6):
    if i == 1:
        continue
    elif i == 4:
        break
    print(i)


