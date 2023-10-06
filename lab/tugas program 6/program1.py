# Swap function
# membuat fungsi swapList untuk menukar index pertama & terakhir
def swapList(newList):
    size = len(newList)

    # Swapping
    # kode dimana isi index pertama & terakhir ditukar
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


# Driver code
# membuat list newList dan mengisinya dengan angka
newList = [12, 35, 9, 56, 24]

# print list dengan memanggil fungsi swapList
print(swapList(newList))
