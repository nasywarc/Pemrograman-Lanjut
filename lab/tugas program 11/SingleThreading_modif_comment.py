# Nasywa Azizah Zharifah
# 225150307111060

# import module threading dan time
import threading
from time import *

# fungsi sqr selama n detik
def sqr(n):
    for x in n:
        sleep(1)

# fungsi cube selama n detik
def cube(n):
    for x in n:
        sleep(1)

# inisialisasi list n
n = [1,2,3,4,5,6,7,8]

# membuat thread dari masing masing fungsi menjadi target
t1 =threading.Thread(target=sqr, args=(n,))
t2 =threading.Thread(target=cube, args=(n,))

# waktu saat dimulai
start = time()

# memulai threading
t1.start()
t2.start()

# menunggu semua thread selesai
t1.join()
t2.join()

# waktu saat selesai
end = time()

print("Waktu mulai :", start)
print("Waktu selesai :", end)
print("Durasi eksekusi program:", end-start)

