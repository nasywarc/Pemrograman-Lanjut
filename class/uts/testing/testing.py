import os
import csv

def search_by_name (search) :
    search_lower = search.lower()
    search_capital = search.capitalize()
    search_title = search.title()
    with open("C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv", "r", newline='', encoding="cp437", errors='ignore') as new_york:
        read_file = csv.DictReader(new_york)
        print('\n--------------------------------------------------------------')
        print("\nResult :")
        global found
        for row in read_file :
            if search in row['name']:
                found = True
                print(f"ID = {row['id']}\nName = {row['name']}\n")
            elif search_lower in row['name']:
                found = True
                print(f"ID = {row['id']}\nName = {row['name']}\n")
            elif search_capital in row['name'] :
                found = True
                print(f"ID = {row['id']}\nName = {row['name']}\n")
            elif search_title in row['name']:
                found = True
                print(f"ID = {row['id']}\nName = {row['name']}\n")
        print('\n==============================================================')
        if found == False :
            print(f"There is no name such \"{search}\"")

def search_by_id (search) :
    with open("C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv", "r", newline='', encoding="cp437", errors='ignore') as new_york:
        read_file = csv.DictReader(new_york)
        print('\n--------------------------------------------------------------')
        print("\nResult :")
        global found
        for row in read_file :
            if search == row['id']:
                found = True
                print(f"ID = {row['id']}\nName = {row['name']}\n")
        print('==============================================================')
        if found == False :
            print(f"There is no ID such \"{search}\"")

os.system('cls')
print('''
==============================================================
                    NEW YORK HOUSING FINDER
==============================================================
'''
)
found = False
search_by = input("Search by (\'ID\' or \'Name\'):\nInput -> ")
if search_by == "ID" or search_by == "id" :
    search = input("\nSearch : \nInput ID -> ")
    search_by_id(search)
elif search_by == "Name" or search_by == "name" :
    search = input("\nSearch : \nInput Name -> ")
    search_by_name(search)