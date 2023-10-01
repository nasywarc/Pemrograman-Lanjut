# PROGRAM 2
# Nama    : Nasywa Azizah Zharifah
# NIM     : 225150307111060

# membuat variabel input_user untuk selanjutnya diambil huruf ke-0, 2 dan 4nya
input_user = input(
    "Masukkan tiga angka untuk mewakili tinggi, lebar, serta ketebalan.\n")

# sebagai tinggi
m = int(input_user[0])
# sebagai lebar
n = int(input_user[2])
# sebagai ketebalan
l = int(input_user[4])

print("\n")

# membuat looping untuk membentuk huruf c
# selama i_tinggi masih termasuk range m
for i_tinggi in range(m):

    # selama j_lebar masih termasuk range n
    for j_lebar in range(n):

        # membuat kondisi dimana jika i_tinggi >= m-l
        # atau j_lebar < l
        # atau i_tinggi < l
        # maka mengoutputkan "*"
        if (i_tinggi >= m - l or j_lebar < l or i_tinggi < l):
            print('*', end='')

        # namun jika kondisi di atas tidak terpenuhi,
        # akan mengoutputkan "."
        else:
            print('.', end='')

    print('')
