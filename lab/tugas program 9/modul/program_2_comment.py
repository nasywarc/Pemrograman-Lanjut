# penginisialan variable x yang sebelumnya dicomment
# x = "Hi!"     #commented

# menggunakan perintah try untuk mencoba mengeksekusi kode dalam blok kode try
try:
    # menampilkan x
    print(x)
# menangkap NameError jika terjadi error    
except NameError:
    print("Variable x is not defined")
# menangkap TypeError jika terjadi error
except TypeError:
    print("Something else went wrong")
# kondisi jika tidak terjadi error
else:
    print("Nothing went wrong")