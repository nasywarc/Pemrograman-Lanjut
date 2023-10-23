class Orang:

    # variabel class, untuk menghitung jumlah orang
    total = 0

    def __init__(self, nama, umur, jurusan):
        #  inisialisasi data, data yang dibuat pada self merupakan variabel object
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan

        # ketika ada orang yang dibuat, tambahkan orang 
        Orang.total += 1

    def __del__(self):
        # kurangi total orang jika object dihapus
        Orang.total -= 1

    def katakanHalo(self):
        print(f"Halo, nama saya {self.nama} umur {self.umur} dari jurusan {self.jurusan}, apa kabar?")

    def total_populasi(cls):
        print(f"Total orang, {cls.total}")

    # method class
    total_populasi = classmethod(total_populasi)

orang = []
loop = True

while loop:

    nama_orang = input('Masukkan nama\t\t: ')
    umur_orang = input('Masukkan umur\t\t: ')
    jurusan_orang = input('Masukkan jurusan\t: ')
    orang.append(Orang(nama_orang, umur_orang, jurusan_orang))

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

        del orang[len(orang)-1]

        print('')

        for semua_orang in orang :
            semua_orang.katakanHalo()

        if len(orang) == 0 :
            del orang
            print('Semua orang sudah terhapus.')
            loop = False
    else :
        loop = False

    Orang.total_populasi()

# print(f'{Orang.total_populasi()}')

# org = Orang('Budi')
# org.katakanHalo()
# Orang.total_populasi()

# org2 = Orang('Andi')
# org2.katakanHalo()
# Orang.total_populasi()

# print("Object dihapus")
# del org
# del org2

# Orang.total_populasi()