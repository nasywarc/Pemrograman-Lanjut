# Nasywa Azizah Zharifah
# 225150307111060

# menginisialisasi posisi awal pada (1, 1)
x = y = 1

# membuat fungsi untuk menghitung banyak cara keluar dari maze
def maze(length, width, x, y):
    if x == length and y == width:
        return 1
    if x > length or y > width:
        return 0
    return maze(length, width, x + 1, y) + maze(length, width, x, y + 1)

# menyimpan variable tinggi dan lebar dalam bentuk integer
tinggi = int(input("Tinggi maze: "))
lebar = int(input("Lebar maze: "))

# memanggil fungsi maze sekaligus menampilkan hasilnya ke user
print(maze(tinggi, lebar, x, y))