import os
import csv

os.system('cls')
search = input("Search : \n")
search_lower = search.lower()
search_capital = search.capitalize()
search_title = search.title()

with open("C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv", "r", newline='', encoding="cp437", errors='ignore') as new_york:
    read_file = csv.DictReader(new_york)
    print("\nResult :")
    for column in read_file :
        if search_lower in column['name']:
            print(f"{column['name']}")
        elif search_capital in column['name'] :
            print(f"{column['name']}")
        elif search_title in column['name']:
            print(f"{column['name']}")