import os
import csv

def search_by_name (search) :
    search_lower = search.lower()
    search_capital = search.capitalize()
    search_title = search.title()
    with open("C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv", "r", newline='', encoding="cp437", errors='ignore') as new_york:
        read_file = csv.DictReader(new_york)
        print("\nResult :")
        for row in read_file :
            if search_lower in row['name']:
                found = True
                print(f"{row['name']}")
            elif search_capital in row['name'] :
                found = True
                print(f"{row['name']}")
            elif search_title in row['name']:
                found = True
                print(f"{row['name']}")
        if found == False :
            print(f"There is no name such \"{search}\"")

def search_by_id (search) :
    with open("C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv", "r", newline='', encoding="cp437", errors='ignore') as new_york:
        read_file = csv.DictReader(new_york)
        print("\nResult :")
        for row in read_file :
            if search == row['id']:
                print(f"{row['id']}\t{row['name']}")


os.system('cls')
found = False
search_by = input("Search by (\'ID\' or \'Name\'):\nInput --> ")
search = input("Search : \nInput --> ")
if search_by == "ID" or search_by == "id" :
    search_by_id(search)
elif search_by == "Name" or search_by == "name" :
    search_by_name(search)

# with open("C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv", "r", newline='', encoding="cp437", errors='ignore') as new_york:
#         read_file = csv.DictReader(new_york)
#         for row in read_file :
#              print(row['name'])


