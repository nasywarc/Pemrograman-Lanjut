# PROGRAM 1
# Nama    : Nasywa Azizah Zharifah
# NIM     : 225150307111060

# membuat variabel angka_user untuk menyimpan nilai input dari user
angka_user = int(input("Masukkan tahun yang ingin Anda cek.\n"))

# kondisi 1
# membuat kondisi dimana jika input user habis dibagi 400,
# maka sudah pasti merupakan tahun kabisat
if (angka_user % 400 == 0):
    # mengoutputkan hasil pengecekan tahun
    print("Tahun Kabisat.")

# kondisi 2
# membuat kondisi lain dimana jika input user tidak habis
# jika dibagi 400, namun habis dibagi 4,
# maka masuk ke percabangan selanjutnya
elif (angka_user % 4 == 0):

    # jika tidak habis dibagi 400 (kondisi 1),
    # namun habis dibagi 4 dan habis dibagi 100,
    # maka bukan tahun kabisat
    if (angka_user % 100 == 0):
        # mengoutputkan hasil pengecekan tahun
        print("Bukan Tahun Kabisat.")

    # jika tidak habis dibagi 400 (kondisi 1),
    # namun habis dibagi 4 dan tidak habis dibagi 100,
    # maka merupakan tahun kabisat
    else:
        # mengoutputkan hasil pengecekan tahun
        print("Tahun Kabisat.")

# kondisi 3
# kondisi dimana input user tidak habis dibagi 400 maupun 4
# maka sudah pasti bukan merupakan tahun kabisat
else:
    # mengoutputkan hasil pengecekan tahun
    print("Bukan Tahun Kabisat.")
