buku = [] # Variabel global untuk menyimpan data Buku

def show_data(): #fungsi untuk menampilkan data
    if (len(buku)) <= 0 :
        print ("BELUM ADA DATA")
    else:
        for indeks in range (len(buku)):
            print ("[%d] %s" % (indeks, buku[indeks]))
show_data()

def insert_data(): #fungsi untuk menambah data
    buku_baru = input("Judul Buku: ")
    buku.append("buku_baru")
insert_data()

def edit_data(): #fungsi untuk mengedit data
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if (indeks > len(buku)):
        print ("ID Salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru
edit_data()

def delete_data(): #fungsi untuk menghapus data
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks > len(buku)):
        print ("ID salah")
    else:
        buku.remove(buku[indeks])
delete_data()

def show_menu(): #fungsi untuk menampilkan menu
    print ("\n")
    print ("======Menu=====")
    print ("[1] Show Data")
    print ("[2] Insert Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")
    menu = int(input("PILIH MENU>"))
    print ("\n")

    if menu == 1 :
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print ("Salah Pilih!")
    if __name__ == "__main__":
        while(True):
            show_menu()
show_menu()