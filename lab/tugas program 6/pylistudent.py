# PROGRAM Pylistudent
# Nasywa Azizah Zharifah
# 225150307111060

def input_data () :

    input_name = input("Type your name : ")
    input_nim = input("Type your NIM : ")
    input_major = input("Type your major : ")

    dict_data['name'].append(input_name)
    dict_data['nim'].append(input_nim)
    dict_data['major'].append(input_major)

print("Welcome to Pylistudent")

dict_data = {"name" : [], "nim" : [], "major" : []}
loop = True

while loop :
    input_data()
    keep_loop = input("Do you wanna add another data? (Type \"Yes\" or \"No\")\nYour input : ")
    if keep_loop == 'No' or keep_loop == 'no' :
        loop = False
    elif keep_loop == 'Yes' or keep_loop == 'yes' :
        loop = True
    else :
        print("Your input is invalid.")
        loop = False

for name in dict_data['name'] :
    print(name)