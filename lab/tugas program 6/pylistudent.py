# PROGRAM Pylistudent
# Nasywa Azizah Zharifah
# 225150307111060

def input_data () :

    input_name = input("\nType your name\t: ")
    input_nim = input("Type your NIM\t: ")
    input_major = input("Type your major\t: ")

    dict_data['name'].append(input_name)
    dict_data['nim'].append(input_nim)
    dict_data['major'].append(input_major)

print(
'''===================================================
                PYLISTUDENT PROGRAM
==================================================='''
)
print("Welcome to Pylistudent.")
print("This program is created to list student data.")

dict_data = {"name" : [], "nim" : [], "major" : []}
i = 1
loop = True

while loop :
    input_data()
    keep_loop = input("\nDo you wanna add another data? (Type \"Yes\" or \"No\")\nInput : ")
    if keep_loop == 'No' or keep_loop == 'no' :
        loop = False
    elif keep_loop == 'Yes' or keep_loop == 'yes' :
        loop = True
        i+=1
    else :
        print("Your input is invalid.")
        loop = False

print(
'''===================================================
           Creating a list of student......
'''
)
print(
'''===================================================
                  LIST OF STUDENT
==================================================='''
)
for total in range (0, i) : 
    print(f"Student {total+1}")
    print(f"Name\t: {dict_data['name'][total]}")
    print(f"NIM\t: {dict_data['nim'][total]}")
    print(f"Major\t: {dict_data['major'][total]}")
print("==================================================")
