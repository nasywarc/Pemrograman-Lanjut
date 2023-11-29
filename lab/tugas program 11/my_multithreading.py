from time import *
import threading

def print_name(n):
    for let in n:
        print (let, end='')
        sleep(1)
        
first_name = ['N', 'a', 's', 'y', 'w', 'a']
mid_name = ['A', 'z', 'i', 'z', 'a', 'h']
last_name = ['Z', 'h', 'a', 'r', 'i', 'f', 'a', 'h']

t1 = threading.Thread(target=print_name, args=(first_name, ))
t2 = threading.Thread(target=print_name, args=(mid_name, ))
t3 = threading.Thread(target=print_name, args=(last_name, ))

start = time()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time()
duration = end - start
print(f'Duration : {duration}')