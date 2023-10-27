# PROGRAM PYCLASS
# Nasywa Azizah Zharifah
# 225150307111060

import os

class Tugas:

    total = 0

    def __init__(self, nama_matkul, materi, deadline, apakah_selesai):
        self.mk = nama_matkul
        self.materi = materi
        self.tgl = deadline
        self.status = apakah_selesai

        Tugas.total += 1

    def __del__(self):
        Tugas.total -= 1

    def print_tugas(self):
        print(f'Mata Kuliah\t: {self.mk}')
        print(f'Materi\t\t: {self.materi}')
        print(f'Batas Akhir\t: {self.tgl}')
        print(f'Status\t\t: {self.status}')

    def ubah_status(self):
        pass

    def total_tugas(cls):
        print(f'\nJumlah tugas\t: {cls.total}')

    total_tugas = classmethod(total_tugas)

daftar_tugas = []
loop = True

os.system('cls')

while loop:
    
    # prompt untuk user mengisi data
    # akan dimasukkan ke list orang dalam bentuk Tugas
    matakuliah = input('Masukkan Mata Kuliah\t\t: ')
    materi_tugas = input('Masukkan Materi Tugas\t\t: ')
    deadline_tugas = input('Masukkan Batas Pengumpulan\t: ')
    status_tugas = 'Belum Dikerjakan'
    daftar_tugas.append(Tugas(matakuliah, materi_tugas, deadline_tugas, status_tugas))
    
    # prompt apakah ingin menambahkan lagi
    menambah_tugas = input('\nApa Anda ingin daftar tugas lagi? "Ya" atau "Tidak".\nInput -> ').lower()

    if menambah_tugas == 'tidak':
        loop = False
    elif menambah_tugas != 'ya':
        print('Input anda tidak valid.')
        loop = False
    
    print('')

os.system('cls')
print('--------------')
print('| LIST TUGAS |')
print('--------------')

# menampilkan semua object untuk ditampilkan
for index in range(len(daftar_tugas)) :
    print(f'Tugas ke-{index+1}')
    daftar_tugas[index].print_tugas()
    print('')

# menampilkan total populasi
Tugas.total_tugas()

loop = True

while loop :
    # prompt apa ingin menghapus orang
    menghapus_tugas = input('\nApa Anda ingin menghapus tugas? "Ya" atau "Tidak".\nInput -> ').lower()
    
    # jika iya, akan menghapus orang yang berada di akhir list
    if menghapus_tugas == 'ya':
        if daftar_tugas :
            del daftar_tugas[-1]

            print('')
            
            # menampilkan katakanHalo untuk semua object yang tersisa
            for index in range(len(daftar_tugas)) :
                print(f'Tugas ke-{index+1}')
                daftar_tugas[index].print_tugas()
                print('')
            
            # jika len(orang) sudah 0, akan menghapus paksa object
            if len(daftar_tugas) == 0 :
                Tugas.__del__(daftar_tugas)
                print('Semua tugas sudah terhapus.')
                loop = False

    elif menghapus_tugas == 'tidak' :
        print('')
        loop = False
    else :
        print('\nInput anda tidak valid.')
        loop = False

    # menampilkan total populasi yang tersisa
    Tugas.total_tugas()
