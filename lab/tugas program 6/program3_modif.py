# mengimport Counter dari module collections
from collections import Counter

# fungsi untuk menghilangkan kata yang muncul lebih dari 1x
def remov_duplicates(input):

    input = input.split(" ") # memisahkan var input dg spasi sbg separatornya

    for i in range(0, len(input)): 
        input[i] = "".join(input[i]) # loop untuk menggabungkan input kembali
    
    UniqW = Counter(input) # counter untuk menghitung elemen yg sama dalam var input

    s = " ".join(UniqW.keys()) # menggabungkan setiap key/kunci dari dictionary UniqW
    print(s)

if __name__ == "__main__": # akan berjalan jika program ini dijalankan sbg program utama
    input = 'Python is great and Java is also great'
    remov_duplicates(input) # memanggil fungsi remov_duplicates
