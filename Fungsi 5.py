#membuat kakulator sederhana

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y

print("Kalkulator Uzan")
print("Silahkan Dipilih")
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Masukkan pilihan (1/2/3/4): ")
bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

if pilihan == '1':
    print(bilangan1, "+", bilangan2, "=", tambah(bilangan1, bilangan2))

elif pilihan == '2':
    print(bilangan1, "-", bilangan2, "=", kurang(bilangan1, bilangan2))

elif pilihan == '3':
    print(bilangan1, "*", bilangan2, "=", kali(bilangan1, bilangan2))

elif pilihan == '4':
    print(bilangan1, "/", bilangan2, "=", bagi(bilangan1, bilangan2))

else:
    print("Salah Pilih jangan itu yaa")