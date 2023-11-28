# Nasywa Azizah Zharifah
# 225150307111060


import threading
from time import *

def sqr(n):
    for x in n:
        sleep(1)
        
def cube(n):
    for x in n:
        sleep(1)

        
n = [1,2,3,4,5,6,7,8]

t1 =threading.Thread(target=sqr, args=(n,))
t2 =threading.Thread(target=cube, args=(n,))

start = time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time()

print("Waktu mulai :", start)
print("Waktu selesai :", end)
print("Durasi eksekusi program:", end-start)

