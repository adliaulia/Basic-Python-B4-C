#jika perulangan di dalam perulangan
for i in range(2):
    #print("i =",i)
    for j in range(3):
        #print("j =",j)
        print("{} {}".format(i,j), end=" ")
    print()
#maka perulangan pada loop didalam yang akan dikerjakan dulu sampai selesai

print()
list_data=[[1,2],[3,4]]
for i in list_data:
    for j in i:
        print(j*5)