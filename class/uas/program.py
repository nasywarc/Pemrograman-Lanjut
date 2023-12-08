# string1 = '     Halo     '
# string2 = 'Semua    '

# print(len(string1))
# print(len(string1.strip()))
# print(len(string2))
# print(len(string2.strip()))

# print(string1)
# print(string1.lstrip())
# print(len(string1.rstrip().lstrip()))
# print(len(string1.rstrip()))
# print(len(string2.rstrip()))


# a = 10
# print(a)
# a += int('10', 2)
# print(a)
# a += int('10', 8)
# print(a)
# a += int('0x10', 16)
# print(a)
# print(bin(2))

string = 'pemrograman'
print(string[-5:])
print(string[-5:-3])

file = open('contoh_file.txt', 'a')
file.write('\nline lima')
file.close()