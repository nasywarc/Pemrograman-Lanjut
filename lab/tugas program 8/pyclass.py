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
    matakuliah = input('Masukkan Mata Kuliah : ')
    materi_tugas = input('Masukkan Deskripsi Tugas : ')
    deadline_tugas = input('Masukkan Batas Pengumpulan : ')
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


