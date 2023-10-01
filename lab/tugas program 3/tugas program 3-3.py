# PROGRAM 3
# Nama    : Nasywa Azizah Zharifah
# NIM     : 225150307111060

# membuat variabel n_bilangan untuk menentukan
# berapa angka genap yang ingin user simpan
n_bilangan = input("Jumlah angka genap yang ingin disimpan : ")

# membuat variabel boolean bernilai True
bool = True

print("\n")

# membuat variabel bernilai awal 0 untuk menghitung sudah berapa input
# yang merupakan angka genap
hitung_input = 0

# membuat loop terus berjalan selama boolean bernilai True
while (bool == True):

    # membuat variabel cek_angka untuk selanjutnya dicek
    cek_angka = input("Masukkan angka : ")

    # membuat kondisi 1 jika int dari cek_angka user habis dibagi 2
    if (int(cek_angka) % 2 == 0):
        # mengoutputkan angka jika angka genap
        print(cek_angka, "\n")

        # variabel hitung input akan ter-increment
        # (seolah olah tersimpan)
        hitung_input += 1

        # jika var hitung_input sudah mencapai n_bilangan yang diinput user
        # maka boolean akan berganti nilai menjadi false, dan looping akan berhenti
        if (hitung_input == int(n_bilangan)):
            bool = False

    # membuat kondisi lain jika kondisi 1 tidak terpenuhi
    else:
        # akan mengoutputkan angka tersebut bukan angka genap
        print("Bukan angka genap!\n")
