# PROGRAM PYCLASS
# Nasywa Azizah Zharifah
# 225150307111060

class Tugas:

    total = 0

    def __init__(self, nama_matkul, deskripsi, deadline, apakah_selesai):
        self.mk = nama_matkul
        self.deskripsi = deskripsi
        self.tgl = deadline
        self.status = apakah_selesai

    def __del__(self):
        Tugas.total -= 1

    def print_tugas(self):
        print(f'Mata Kuliah\t: {self.mk}')
        print(f'Deskripsi\t: {self.deskripsi}')
        print(f'Batas Akhir\t: {self.tgl}')
        print(f'Status\t: {self.status}')

    def ubah_status(self):
        pass

    def total_tugas(cls):
        print(f'Jumlah tugas\t: {cls.total}')

    total_tugas = classmethod(total_tugas)

daftar_tugas = []
loop = True

while loop:
    
    # prompt untuk user mengisi data
    # akan dimasukkan ke list orang dalam bentuk Orang
    matakuliah = input('Masukkan mata kuliah : ')
    deskripsi_tugas = input('Masukkan deskripsi : ')
    deadline_tugas = input('Masukkan batas pengumpulan : ')
    status_tugas = 'belum selesai'
    daftar_tugas.append(Tugas(matakuliah, deskripsi_tugas, status_tugas))
    
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


        # print('----------')
        # print('LIST TUGAS')
        # print('----------')
