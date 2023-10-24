# Nasywa Azizah Zharifah
# 225150307111060

# membuat class bernama Orang
class Orang:

    # variabel class, untuk menghitung jumlah orang
    total = 0

    def __init__(self, nama, fakultas, jurusan):
        #  inisialisasi data, data yang dibuat pada self merupakan variabel object
        # membuat tiga atribut, yaitu nama, fakultas, dan jurusan
        self.nama = nama
        self.fakultas = fakultas
        self.jurusan = jurusan

        # ketika ada orang yang dibuat, tambahkan orang 
        Orang.total += 1

    def __del__(self):
        # kurangi total orang jika object dihapus
        Orang.total -= 1
    
    # membuat fungsi untuk menampilkan object untuk mengatakan halo
    def katakanHalo(self):
        print(f"Halo, nama saya {self.nama} dari Fakultas {self.fakultas}, Jurusan {self.jurusan}. Apa kabar?")
    
    # fungsi untuk menampilkan jumlah object
    def total_populasi(cls):
        print(f"Total orang, {cls.total}")

    # method class
    total_populasi = classmethod(total_populasi)

# membuat list orang dan loop
orang = []
loop = True

while loop:
    
    # prompt untuk user mengisi data
    # akan dimasukkan ke list orang dalam bentuk Orang
    nama_orang = input('Masukkan nama : ')
    fakultas_orang = input('Masukkan fakultas : ')
    jurusan_orang = input('Masukkan jurusan : ')
    orang.append(Orang(nama_orang, fakultas_orang, jurusan_orang))
    
    # prompt apakah ingin menambahkan lagi
    menambah_orang = input('\nApa Anda ingin menambah orang lagi? "Ya" atau "Tidak".\nInput -> ').lower()

    if menambah_orang == 'tidak':
        loop = False
    elif menambah_orang != 'ya':
        print('Input anda tidak valid.')
        loop = False
    
    print('')

# menampilkan semua object untuk mengatakan halo
for semua_orang in orang :
    semua_orang.katakanHalo()

# menampilkan total populasi
Orang.total_populasi()

loop = True

while loop :
    # prompt apa ingin menghapus orang
    menghapus_orang = input('\nApa Anda ingin menghapus orang? "Ya" atau "Tidak".\nInput -> ').lower()
    
    # jika iya, akan menghapus orang yang berada di akhir list
    if menghapus_orang == 'ya':
        if orang :
            del orang[-1]

            print('')
            
            # menampilkan katakanHalo untuk semua object yang tersisa
            for semua_orang in orang :
                semua_orang.katakanHalo()
            
            # jika len(orang) sudah 0, akan menghapus paksa object
            if len(orang) == 0 :
                Orang.__del__(orang)
                print('Semua orang sudah terhapus.')
                loop = False
    elif menghapus_orang == 'tidak' :
        print('')
        loop = False
    else :
        print('\nInput anda tidak valid.')
        loop = False

    # menampilkan total populasi yang tersisa
    Orang.total_populasi()