def check(original, edited):
    if original == edited :
        print('Palindrom')
    else :
        print('Bukan palindrom')

def reversed(word):
    return word[::-1]

kata = []
n = int(input("Jumlah huruf yang ingin diperiksa : "))

for i in range(n):
    kata.append(input("Tuliskan sebuah kata : "))

for i in range(n) :
    check(kata[i], reversed(kata[i]))