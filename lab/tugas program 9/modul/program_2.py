# Nasywa Azizah Zharifah
# 225150307111060

# x = "Hi!"     #commented

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except TypeError:
    print("Something else went wrong")
else:
    print("Nothing went wrong")