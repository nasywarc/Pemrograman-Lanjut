x = y = 1

def maze(length, width, x, y):
    if x == length and y == width:
        return 1
    if x > length or y > width:
        return 0
    return maze(length, width, x + 1, y) + maze(length, width, x, y + 1)

tinggi = int(input("Tinggi maze: "))
lebar = int(input("Lebar maze: "))
print(maze(tinggi, lebar, x, y))