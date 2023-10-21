# Nasywa Azizah Zharifah
# 225150307111060

# membuat fungsi untuk mengecek persamaan
def check(original, edited):
    if original == edited :
        print('Palindrom')
    else :
        print('Bukan palindrom')

# membuat fungsi untuk membalikkan kata
def reversed(word):
    return word[::-1]

# membuat list untuk menampung var kata
kata = []
n = int(input("Jumlah huruf yang ingin diperiksa : "))

# looping untuk menyimpan nilai list kata
for i in range(n):
    kata.append(input("Tuliskan sebuah kata : "))

# looping untuk memanggil fungsi check sekaligus reversed
for i in range(n) :
    check(kata[i], reversed(kata[i]))