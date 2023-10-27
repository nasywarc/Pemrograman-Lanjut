# PROGRAM PYCLASS
# Nasywa Azizah Zharifah
# 225150307111060

import os

class Tugas:

    total = 0

    def __init__(self, nama_matkul, deskripsi, deadline, apakah_selesai):
        self.mk = nama_matkul
        self.deskripsi = deskripsi
        self.tgl = deadline
        self.status = apakah_selesai

        Tugas.total += 1

    def __del__(self):
        Tugas.total -= 1

    def print_tugas(self):
        print(f'Mata Kuliah\t: {self.mk}')
        print(f'Deskripsi\t: {self.deskripsi}')
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
    # akan dimasukkan ke list orang dalam bentuk Orang
    matakuliah = input('Masukkan mata kuliah : ')
    deskripsi_tugas = input('Masukkan deskripsi : ')
    deadline_tugas = input('Masukkan batas pengumpulan : ')
    status_tugas = 'belum selesai'
    daftar_tugas.append(Tugas(matakuliah, deskripsi_tugas, deadline_tugas, status_tugas))
    
    # prompt apakah ingin menambahkan lagi
    menambah_orang = input('\nApa Anda ingin menambah orang lagi? "Ya" atau "Tidak".\nInput -> ').lower()

    if menambah_orang == 'tidak':
        loop = False
    elif menambah_orang != 'ya':
        print('Input anda tidak valid.')
        loop = False
    
    print('')

print('--------------')
print('| LIST TUGAS |')
print('--------------')

# menampilkan semua object untuk mengatakan halo
for semua_tugas in daftar_tugas :
    semua_tugas.print_tugas()

# menampilkan total populasi
Tugas.total_tugas()


