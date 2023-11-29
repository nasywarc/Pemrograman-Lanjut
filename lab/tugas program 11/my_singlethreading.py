from time import *

def first(n):
    for let in n:
        print (let, end='')
        sleep(1)

def second(n):
    for let in n:
        print (let, end='')
        sleep(1)
        
def third(n):
    for let in n:
        print (let, end='')
        sleep(1)
        
first_name = ['N', 'a', 's', 'y', 'w', 'a']
mid_name = ['A', 'z', 'i', 'z', 'a', 'h']
last_name = ['Z', 'h', 'a', 'r', 'i', 'f', 'a', 'h']

start = time()

first(first_name)
print('\n')
second(mid_name)
print('\n')
third(last_name)
print('\n')

end = time()

duration = end - start

print(f'Duration : {duration}')