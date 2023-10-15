import os
import csv

def search_by_name (search) :
    search_lower = search.lower()
    search_capital = search.capitalize()
    search_title = search.title()
    i = 1
    with open("C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv", "r", newline='', encoding="cp437", errors='ignore') as new_york:
        read_file = csv.DictReader(new_york)
        print('\n--------------------------------------------------------------')
        print("\nResult :\n")
        global found
        for row in read_file :
            if search in row['name'] or search_lower in row['name'] or search_capital in row['name'] or search_title in row['name']:
                found = True
                print(f"Data - {i}")
                print(f"\tID = {row['id']}\n\tName = {row['name']}\n\tHost Name =  {row['host_name']}\n\tNeightbourhood Group = {row['neighbourhood_group']}\n\tNeighbourhood = {row['neighbourhood']}\n\tLatitude = {row['latitude']}\n\tLongtitude = {row['longitude']}\n\tRoom Type = {row['room_type']}\n\tPrice = {row['price']}\n\tMinimum Nights = {row['minimum_nights']}\n\tNumber of Reviews = {row['number_of_reviews']}\n\tLast Review = {row['last_review']}\n\tReviews per Month = {row['reviews_per_month']}\n\tCalculated Host Listing Count = {row['calculated_host_listings_count']}\n\tAvailability = {row['availability_365']}\n")
                i += 1
        if found == False :
            print(f"There is no name such \"{search}\"")

def search_by_id (search) :
    with open("C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv", "r", newline='', encoding="cp437", errors='ignore') as new_york:
        read_file = csv.DictReader(new_york)
        print('\n--------------------------------------------------------------')
        print("\nResult :\n")
        global found
        for row in read_file :
            if search == row['id']:
                found = True
                print(f"ID = {row['id']}\nName = {row['name']}\nHost Name =  {row['host_name']}\nNeightbourhood Group = {row['neighbourhood_group']}\nNeighbourhood = {row['neighbourhood']}\nLatitude = {row['latitude']}\nLongtitude = {row['longitude']}\nRoom Type = {row['room_type']}\nPrice = {row['price']}\nMinimum Nights = {row['minimum_nights']}\nNumber of Reviews = {row['number_of_reviews']}\nLast Review = {row['last_review']}\nReviews per Month = {row['reviews_per_month']}\nCalculated Host Listing Count = {row['calculated_host_listings_count']}\nAvailability = {row['availability_365']}")
        if found == False :
            print(f"There is no ID such \"{search}\"")

os.system('cls')
print('''
==============================================================
                    NEW YORK HOUSING FINDER
=============================================================='''
)
found = False
loop = True
while loop :
    search_by = input("\nSearch by (\'ID\' or \'Name\') or type \"exit\" to leave program :\nInput -> ")
    if search_by == "ID" or search_by == "id" :
        search = input("\nSearch : \nInput ID -> ")
        search_by_id(search)
    elif search_by == "Name" or search_by == "name" :
        search = input("\nSearch : \nInput Name -> ")
        search_by_name(search)
    elif search_by == "exit" :
        print("\nSTATUS : EXIT")
        print('==============================================================')
        loop = False
    else:
        print("Your input is invalid.\n")
