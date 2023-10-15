import os
import csv
import art

def search_by_name (search) :
    i = 1
    with open("C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv", "r", newline='', encoding="cp437", errors='ignore') as new_york:
        read_file = csv.DictReader(new_york)
        print("\nResult :\n")
        global found
        for row in read_file :
            if search.lower() in row['name'].lower():
                found = True
                print(f"Data - {i}")
                print(f"\tID = {row['id']}\n\tName = {row['name']}\n\tHost Name =  {row['host_name']}\n\tNeightbourhood Group = {row['neighbourhood_group']}\n\tNeighbourhood = {row['neighbourhood']}\n\tLatitude = {row['latitude']}\n\tLongtitude = {row['longitude']}\n\tRoom Type = {row['room_type']}\n\tPrice = {row['price']}\n\tMinimum Nights = {row['minimum_nights']}\n\tNumber of Reviews = {row['number_of_reviews']}\n\tLast Review = {row['last_review']}\n\tReviews per Month = {row['reviews_per_month']}\n\tCalculated Host Listing Count = {row['calculated_host_listings_count']}\n\tAvailability = {row['availability_365']}\n")
                i += 1
        if found == False :
            print(f"There is no name such \"{search}\"\n")

def search_by_id (search) :
    with open("C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv", "r", newline='', encoding="cp437", errors='ignore') as new_york:
        read_file = csv.DictReader(new_york)
        print("\nResult :\n")
        global found
        for row in read_file :
            if search == row['id']:
                found = True
                print("Data")
                print(f"\tID = {row['id']}\n\tName = {row['name']}\n\tHost Name =  {row['host_name']}\n\tNeightbourhood Group = {row['neighbourhood_group']}\n\tNeighbourhood = {row['neighbourhood']}\n\tLatitude = {row['latitude']}\n\tLongtitude = {row['longitude']}\n\tRoom Type = {row['room_type']}\n\tPrice = {row['price']}\n\tMinimum Nights = {row['minimum_nights']}\n\tNumber of Reviews = {row['number_of_reviews']}\n\tLast Review = {row['last_review']}\n\tReviews per Month = {row['reviews_per_month']}\n\tCalculated Host Listing Count = {row['calculated_host_listings_count']}\n\tAvailability = {row['availability_365']}\n")
        if found == False :
            print(f"There is no ID such \"{search}\"\n")

os.system('cls')
print(art.logo)
found = False
loop = True
run_again = 0
while loop :
    if run_again > 0 :
        os.system('cls')
        print(art.logo)
    print('============================================================')
    search_by = input("1. Search by ID\n2. Search by Name\n3. Exit\nInput (1 / 2 / 3) -> ")
    if search_by == '1' :
        search = input("\nInput ID -> ")
        search_by_id(search)
    elif search_by == '2' :
        search = input("\nInput Name -> ")
        search_by_name(search)
    elif search_by == '3' :
        print("\nThe program has been stopped.")
        print('============================================================')
        loop = False
    else:
        print("\nYour input is invalid.")
        print('============================================================')
        loop = False
    if search_by != '3' :
        keep_run = input("Do you want to continue?\nInput (Yes / No) -> ").lower()
        if keep_run == 'yes' :
            run_again += 1
        elif keep_run == 'no'  :
            print("\nThe program has been stopped.")
            print('============================================================')
            loop = False
        else :
            print("\nYour input is invalid.")
            print('============================================================')
            loop = False