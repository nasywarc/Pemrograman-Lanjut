# Nasywa Azizah Zharifah
# # 225150307111060

class Orang:

    # variabel class, untuk menghitung jumlah orang
    total = 0

    def __init__(self, nama):
        #  inisialisasi data, data yang dibuat pada self merupakan variabel object
        self.nama = nama

        # ketika ada orang yang dibuat, tambahkan orang 
        Orang.total += 1

    def __del__(self):
        # kurangi total orang jika object dihapus
        Orang.total -= 1
    # membuat fungsi untuk menampilkan halo + nama
    def katakanHalo(self):
        print(f"Halo, nama saya {self.nama}, apa kabar?")
    
    # membuat fungsi untuk menampilkan total orang
    def total_populasi(cls):
        print(f"Total orang, {cls.total}")

    # method class
    total_populasi = classmethod(total_populasi)

# membuat object orang bernama Budi
org = Orang('Budi')
# memanggil fungsi agar Budi mengatakan halo
org.katakanHalo()
# menampilan total populasi/orang
Orang.total_populasi()

# membuat object orang bernama Andi
org2 = Orang('Andi')
# memanggil fungsi agar Andi mengatakan halo
org2.katakanHalo()
# menampilan total populasi/orang
Orang.total_populasi()

# menghapus object org dan org2
print("Object dihapus")
del org
del org2

# menampilkan total populasi setelah object dihaous
Orang.total_populasi()