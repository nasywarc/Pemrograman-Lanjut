# membuat fungsi yang mereverse sebuah tuple
def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


# Driver Code
# membuat sebuah tuple lalu memanggil fungsi Reverse dan menampilkannya
tuples = ('z', 'a', 'd', 'f', 'g', 'e', 'e', 'k')
print(Reverse(tuples))
