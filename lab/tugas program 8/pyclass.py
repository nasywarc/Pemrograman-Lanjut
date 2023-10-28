# PROGRAM PYCLASS
# Nasywa Azizah Zharifah
# 225150307111060

# diperlukan untuk membersihkan terminal
import os

# membuat class bernama Tugas
class Tugas:

    total = 0

    # method untuk menginisialisasi object Tugas
    def __init__(self, nama_matkul, materi, deadline, apakah_selesai):
        self.mk = nama_matkul
        self.materi = materi
        self.tgl = deadline
        self.status = apakah_selesai

        Tugas.total += 1

    # method untuk menghapus object
    def __del__(self):
        Tugas.total -= 1

    # method untuk menampilkan semua object Tugas
    def print_tugas(self):
        print(f'\tMata Kuliah\t: {self.mk}')
        print(f'\tMateri\t\t: {self.materi}')
        print(f'\tBatas Akhir\t: {self.tgl}')
        print(f'\tStatus\t\t: {self.status}')

    # method untuk mengubah status object Tugas
    def ubah_status(self):
        self.status = 'Selesai'

    # method untuk menampilkan total object Tugas
    def total_tugas(cls):
        print(f'\nJumlah tugas\t: {cls.total}')

    def cek_status(self):
        if self.status == 'Selesai' :
            return True

    # method class
    total_tugas = classmethod(total_tugas)

# membuat list untuk object Tugas, loop untuk program terus berjalan
daftar_tugas = []
program = True

# selama program True
while program:
    # memberikan pilihan ke user
    os.system('cls')
    print('Selamat datang di program Pyclass. Silakan pilih salah satu dari menu di bawah :')
    print('1. Menambahkan tugas ke daftar.')
    print('2. Menampilkan tugas di daftar.')
    print('3. Menghapus tugas dari daftar.')
    print('4. Menandai penyelesaian tugas.')
    print('5. Keluar program.')

    pilihan = int(input('Input -> '))
    
    # pilihan untuk menambah tugas ke dalam object Tugas
    if pilihan == 1:
        os.system('cls')
        print('----------------')
        print('| TAMBAH TUGAS |')
        print('----------------')

        loop = True

        # loop untuk tetap menambahkan object Tugas
        while loop:
            # prompt untuk user mengisi data
            matakuliah = input('Masukkan Mata Kuliah\t\t: ')
            materi_tugas = input('Masukkan Materi Tugas\t\t: ')
            deadline_tugas = input('Masukkan Batas Pengumpulan\t: ')
            status_tugas = 'Belum Selesai'
            daftar_tugas.append(Tugas(matakuliah, materi_tugas, deadline_tugas, status_tugas))
            
            # prompt apakah ingin menambahkan lagi
            menambah_tugas = input('\nApa Anda ingin daftar tugas lagi? "Ya" atau "Tidak".\nInput -> ').lower()

            if menambah_tugas == 'tidak':
                loop = False

            elif menambah_tugas != 'ya':
                print('Input anda tidak valid.')
                loop = False

            print('')

    # pilihan untuk menampilkan seluruh object Tugas
    elif pilihan == 2:
        os.system('cls')
        print('--------------')
        print('| LIST TUGAS |')
        print('--------------')

        # menampilkan semua object tugas untuk ditampilkan
        for index in range(len(daftar_tugas)) :
            print(f'Tugas ke-{index+1}')
            daftar_tugas[index].print_tugas()

        # menampilkan total tugas
        if Tugas.total > 0 :
            Tugas.total_tugas()
        # jika tidak ada object sama sekali
        else:
            print('Daftar tugas kosong.')
        
        # prompt untuk melanjutkan program
        lanjut = input('\nLanjutkan program? "Ya" atau "Tidak".\nInput -> ').lower()

        if lanjut != 'ya':
            print('\nProgram dihentikan.')
            program = False

    # pilihan untuk menghapus object Tugas sesuai keinginan user
    elif pilihan == 3:
        os.system('cls')
        print('---------------')
        print('| HAPUS TUGAS |')
        print('---------------')
        
        # jika daftar_tugas memiliki object
        if daftar_tugas :
            for index in range(len(daftar_tugas)) :
                    print(f'Tugas ke-{index+1}')
                    daftar_tugas[index].print_tugas()

            # input ingin menghapus object Tugas yang mana
            hapus = int(input('\nSilakan pilih salah satu yang ingin dihapus.\nInput -> '))   

            if Tugas.cek_status(daftar_tugas[hapus-1]) :
                del daftar_tugas[hapus-1]

            else :
                os.system('cls')
                print('---------------')
                print('| HAPUS TUGAS |')
                print('---------------')
                print('Tugas tidak dapat dihapus karena belum dikerjakan.')
                lanjut = input('\nLanjutkan program? "Ya" atau "Tidak".\nInput -> ').lower()

                if lanjut != 'ya':
                    print('\nProgram dihentikan.')
                    program = False

        # jika daftar_tugas tidak memiliki object
        else:
            print('Tidak ada tugas yang dapat dihapus.')
            lanjut = input('\nLanjutkan program? "Ya" atau "Tidak".\nInput -> ').lower()

            if lanjut != 'ya':
                print('\nProgram dihentikan.')
                program = False

    # pilihan untuk mengubah status object Tugas yang sudah selesai
    elif pilihan == 4 :
        os.system('cls')
        print('---------------')
        print('| UBAH STATUS |')
        print('---------------')
        
        # menampilkan seluruh tugas agar user dapat memilih
        for index in range(len(daftar_tugas)) :
            print(f'Tugas ke-{index+1}')
            daftar_tugas[index].print_tugas()

        # prompt untuk user mengetikkan pilihan object Tugas
        ubah = int(input('\nSilakan pilih salah satu yang ingin diubah.\nInput -> '))
        Tugas.ubah_status(daftar_tugas[ubah-1])

    # pilihan untuk menghentikan program
    elif pilihan == 5:
        print('\nProgram dihentikan.')
        program = False
    
    # jika input tidak sesuai pilihan yang diberikan
    else:
        print('Input Anda tidak valid.')