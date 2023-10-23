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

    def katakanHalo(self):
        print(f"Halo, nama saya {self.nama}, apa kabar?")

    def total_populasi(cls):
        print(f"Total orang, {cls.total}")

    # method class
    total_populasi = classmethod(total_populasi)

org = Orang('Budi')
org.katakanHalo()
Orang.total_populasi()

org2 = Orang('Andi')
org2.katakanHalo()
Orang.total_populasi()

print("Object dihapus")
del org
del org2

Orang.total_populasi()