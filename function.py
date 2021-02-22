#menginisiasi fungsi
def my_function():
    print("Hello semua!")

list_buah= ["apel","mangga","melon"]
def tambah():
    list_buah.append(input("tambah buah: "))
    print(list_buah)

#memanggil fungsi
my_function()
tambah()

#function parameter, sudah trdpt var/parameter
def print_nama(name):
    print("Hello nama saya "+name)
print_nama("adli")

#Function Default Parameter
def fungsi_nama(name=""):
    print("Hello nama saya "+name)
print_nama("adli")

#Function Keyword Parameter
def my_funct(ch1, ch2, ch3):
    print("The oldest is "+ ch1)
my_funct("anakpertama", "anakkedua", "anakketiga")

#function return value
def kali(x):
    return 5 * x
print(kali(5))