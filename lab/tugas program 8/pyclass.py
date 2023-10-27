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

    def total_tugas(cls):
        print(f'Jumlah tugas\t: {cls.total}')

    total_tugas = classmethod(total_tugas)

    
        # print('----------')
        # print('LIST TUGAS')
        # print('----------')
