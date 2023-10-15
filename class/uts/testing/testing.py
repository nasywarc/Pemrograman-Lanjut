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
                print(f"{row['name']}")
            elif search_capital in row['name'] :
                print(f"{row['name']}")
            elif search_title in row['name']:
                print(f"{row['name']}")
            else:
                print(f"There is no name such \"{search}\"")

def search_by_id (search) :
    with open("C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv", "r", newline='', encoding="cp437", errors='ignore') as new_york:
        read_file = csv.DictReader(new_york)
        print("\nResult :")
        for row in read_file :
            if search in row['id']:
                print(f"{row['id']}\t{row['name']}")


os.system('cls')
search = input("Search : \n")
search_by_id(search)

# with open("C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv", "r", newline='', encoding="cp437", errors='ignore') as new_york:
#         read_file = csv.DictReader(new_york)
#         for row in read_file :
#              print(row['name'])


