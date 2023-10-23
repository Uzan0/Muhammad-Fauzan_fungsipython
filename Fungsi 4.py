def hitung_jumlah_angka(daftar_angka, pemisah): #fungsi menerima dua parameter
    jumlah = 0
    for angka in daftar_angka:
        if angka % pemisah == 0:
            jumlah += angka
    return jumlah
daftar_angka = [1, 2, 3, 4, 5]
pemisah = 2
jumlah_angka_bisa_dibagi = hitung_jumlah_angka(daftar_angka, pemisah)
print("Jumlah angka dalam daftar_angka yang bisa dibagi habis oleh", pemisah, "adalah", jumlah_angka_bisa_dibagi)