# Nasywa Azizah Zharifah
# 225150307111060

class Orang:

    # variabel class, untuk menghitung jumlah orang
    total = 0

    def __init__(self, nama, fakultas, jurusan):
        #  inisialisasi data, data yang dibuat pada self merupakan variabel object
        self.nama = nama
        self.fakultas = fakultas
        self.jurusan = jurusan

        # ketika ada orang yang dibuat, tambahkan orang 
        Orang.total += 1

    def __del__(self):
        # kurangi total orang jika object dihapus
        Orang.total -= 1

    def katakanHalo(self):
        print(f"Halo, nama saya {self.nama} dari Fakultas {self.fakultas}, Jurusan {self.jurusan}. Apa kabar?")

    def total_populasi(cls):
        print(f"Total orang, {cls.total}")

    # method class
    total_populasi = classmethod(total_populasi)

orang = []
loop = True

while loop:

    nama_orang = input('Masukkan nama : ')
    fakultas_orang = input('Masukkan fakultas : ')
    jurusan_orang = input('Masukkan jurusan : ')
    orang.append(Orang(nama_orang, fakultas_orang, jurusan_orang))

    menambah_orang = input('\nApa Anda ingin menambah orang lagi? "Ya" atau "Tidak".\nInput -> ').lower()

    if menambah_orang == 'tidak':
        loop = False
    
    print('')

for semua_orang in orang :
    semua_orang.katakanHalo()

Orang.total_populasi()

loop = True

while loop :
    menghapus_orang = input('\nApa Anda ingin menghapus orang? "Ya" atau "Tidak".\nInput -> ').lower()

    if menghapus_orang == 'ya':
        if orang :
            del orang[-1]

            print('')

            for semua_orang in orang :
                semua_orang.katakanHalo()

            if len(orang) == 0 :
                Orang.__del__(orang)
                print('Semua orang sudah terhapus.')
                loop = False
    else :
        print('')
        loop = False

    Orang.total_populasi()