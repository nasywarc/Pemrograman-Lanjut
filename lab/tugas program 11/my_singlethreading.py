from time import *

def print_name(n):
    for let in n:
        print (let, end='')
        sleep(1)
        
first_name = ['N', 'a', 's', 'y', 'w', 'a']
mid_name = ['A', 'z', 'i', 'z', 'a', 'h']
last_name = ['Z', 'h', 'a', 'r', 'i', 'f', 'a', 'h']

start = time()

print_name(first_name)
print('\n')
print_name(mid_name)
print('\n')
print_name(last_name)
print('\n')

end = time()

duration = end - start

print(f'Duration : {duration}')