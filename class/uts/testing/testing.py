import os
import csv
import art

def show () :
    print("show")
    i = 1
    global file_path
    with open(file_path, "r", newline='', encoding="cp437", errors='ignore') as new_york:
        read_file = csv.DictReader(new_york)
        print("\nResult\n------")
        for row in read_file :
            print(f"Data - {i}")
            print(f"\tID = {row['id']}\n\tName = {row['name']}\n\tHost Name =  {row['host_name']}\n\tNeighbourhood Group = {row['neighbourhood_group']}\n\tNeighbourhood = {row['neighbourhood']}\n\tLatitude = {row['latitude']}\n\tLongtitude = {row['longitude']}\n\tRoom Type = {row['room_type']}\n\tPrice = {row['price']}\n\tMinimum Nights = {row['minimum_nights']}\n\tNumber of Reviews = {row['number_of_reviews']}\n\tLast Review = {row['last_review']}\n\tReviews per Month = {row['reviews_per_month']}\n\tCalculated Host Listing Count = {row['calculated_host_listings_count']}\n\tAvailability = {row['availability_365']}\n")
            i += 1

def search_by_name (search) :
    i = 1
    global file_path
    with open(file_path, "r", newline='', encoding="cp437", errors='ignore') as new_york:
        read_file = csv.DictReader(new_york)
        print("\nResult\n------")
        global found
        for row in read_file :
            if search.lower() in row['name'].lower():
                found = True
                print(f"Data - {i}")
                print(f"\tID = {row['id']}\n\tName = {row['name']}\n\tHost Name =  {row['host_name']}\n\tNeighbourhood Group = {row['neighbourhood_group']}\n\tNeighbourhood = {row['neighbourhood']}\n\tLatitude = {row['latitude']}\n\tLongtitude = {row['longitude']}\n\tRoom Type = {row['room_type']}\n\tPrice = {row['price']}\n\tMinimum Nights = {row['minimum_nights']}\n\tNumber of Reviews = {row['number_of_reviews']}\n\tLast Review = {row['last_review']}\n\tReviews per Month = {row['reviews_per_month']}\n\tCalculated Host Listing Count = {row['calculated_host_listings_count']}\n\tAvailability = {row['availability_365']}\n")
                i += 1
        if found == False :
            print(f"There is no name such \"{search}\"\n")

def search_by_id (search) :
    global file_path
    with open(file_path, "r", newline='', encoding="cp437", errors='ignore') as new_york:
        read_file = csv.DictReader(new_york)
        print("\nResult\n------")
        global found
        for row in read_file :
            if search == row['id']:
                found = True
                print("Data")
                print(f"\tID = {row['id']}\n\tName = {row['name']}\n\tHost Name =  {row['host_name']}\n\tNeighbourhood Group = {row['neighbourhood_group']}\n\tNeighbourhood = {row['neighbourhood']}\n\tLatitude = {row['latitude']}\n\tLongtitude = {row['longitude']}\n\tRoom Type = {row['room_type']}\n\tPrice = {row['price']}\n\tMinimum Nights = {row['minimum_nights']}\n\tNumber of Reviews = {row['number_of_reviews']}\n\tLast Review = {row['last_review']}\n\tReviews per Month = {row['reviews_per_month']}\n\tCalculated Host Listing Count = {row['calculated_host_listings_count']}\n\tAvailability = {row['availability_365']}\n")
        if found == False :
            print(f"There is no ID such \"{search}\"\n")

def is_duplicate(rows, id_to_check):
    for row in rows:
        if id_to_check == row['id']:
            return True
    return False

def add () :
    global file_path
    print("You're going to add a new data.\n")
    with open(file_path, "r", newline='', encoding="cp437", errors='ignore') as new_york:
        read_file = csv.DictReader(new_york)
        duplicate = False
        add_ID = input("Enter ID : ")
        for row in read_file :
            if add_ID == row['id']:
                duplicate = True
        while duplicate :
            print("ID has been used.\n")
            add_ID = input("Enter ID : ")
            for row in read_file :
                if add_ID == row['id']:
                    duplicate = True
                else :
                    duplicate = False
            
    add_name = input("Enter name : ")
    add_host_name = input("Enter host name : ")
    add_host_ID = input("Enter host ID : ")
    add_neighb_grp = input("Enter neighbourhood group : ")
    add_neighb = input("Enter neighbourhood : ")
    add_latitude = input("Enter latitude : ")
    add_longtitude = input("Enter longtitude : ")
    add_room_type = input("Enter room type : ")
    add_price = input("Enter price : ")
    add_min_nights = input("Enter minimum nights : ")
    add_num_of_reviews = input("Enter number of reviews : ")
    add_last_review = input("Enter last review : ")
    add_rev_per_mon = input("Enter reviews per month : ")
    add_calc_host = input("Enter calculated host listing count : ")
    add_avail = input("Enter availability : ")

    if os.path.exists(file_path):
        with open(file_path, "a", newline='', encoding="cp437", errors='ignore') as new_york:
            field_names = ['id',
                           'name',
                           'host_id',
                           'host_name',
                           'neighbourhood_group',
                           'neighbourhood','latitude',
                           'longitude',
                           'room_type',
                           'price',
                           'minimum_nights',
                           'number_of_reviews',
                           'last_review',
                           'reviews_per_month',
                           'calculated_host_listings_count',
                           'availability_365']
            writer = csv.DictWriter(new_york, fieldnames=field_names)
            writer.writerow({
                    'id' : add_ID,
                    'name': add_name,
                    'host_id': add_host_ID,
                    'host_name': add_host_name,
                    'neighbourhood_group': add_neighb_grp,
                    'neighbourhood': add_neighb,
                    'latitude': add_latitude,
                    'longitude': add_longtitude,
                    'room_type': add_room_type,
                    'price': add_price,
                    'minimum_nights': add_min_nights,
                    'number_of_reviews': add_num_of_reviews,
                    'last_review': add_last_review,
                    'reviews_per_month': add_rev_per_mon,
                    'calculated_host_listings_count': add_calc_host,
                    'availability_365': add_avail
                    })
            print("\nThe data has been created.")

    else:
        with open(file_path, "x", newline='', encoding="cp437", errors='ignore') as new_york:
            field_names = ['id',
                           'name',
                           'host_id',
                           'host_name',
                           'neighbourhood_group',
                           'neighbourhood','latitude',
                           'longitude',
                           'room_type',
                           'price',
                           'minimum_nights',
                           'number_of_reviews',
                           'last_review',
                           'reviews_per_month',
                           'calculated_host_listings_count',
                           'availability_365']
            writer = csv.DictWriter(new_york, fieldnames=field_names)
            writer.writeheader()
            writer.writerow({
                    'id' : add_ID,
                    'name': add_name,
                    'host_id': add_host_ID,
                    'host_name': add_host_name,
                    'neighbourhood_group': add_neighb_grp,
                    'neighbourhood': add_neighb,
                    'latitude': add_latitude,
                    'longitude': add_longtitude,
                    'room_type': add_room_type,
                    'price': add_price,
                    'minimum_nights': add_min_nights,
                    'number_of_reviews': add_num_of_reviews,
                    'last_review': add_last_review,
                    'reviews_per_month': add_rev_per_mon,
                    'calculated_host_listings_count': add_calc_host,
                    'availability_365': add_avail
                    })
            print("\nThe data has been created.")

def delete(search):
    global file_path
    with open(file_path, "r", newline='', encoding="cp437", errors='ignore') as new_york:
        rows = list(csv.DictReader(new_york))
    for row in rows:
        if search == row['id']:
            rows.remove(row)
            found = True
    if found:
        with open(file_path, "w", newline='', encoding="cp437", errors='ignore') as new_york:
            fieldnames = rows[0].keys()
            writer = csv.DictWriter(new_york, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Data with ID {search} deleted successfully.\n")
    else:
        print(f"There is no ID such \"{search}\"\n")

file_path = "C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv"
os.system('cls')

print(art.logo)
found = False
loop = True
run_again = 0

while loop :

    if run_again > 0 :
        os.system('cls')
        print('============================================================')
        print(art.logo)
    print('============================================================')
    search_by = input("1. Show data\n2. Find data by ID\n3. Find data by Name\n4. Add data\n5. Update data\n6. Delete data\n7. Exit\nInput (1-7) -> ")

    if search_by == '1' :
        show()
    elif search_by == '2' :
        search = input("\nInput ID -> ")
        search_by_id(search)
    elif search_by == '3' :
        search = input("\nInput Name -> ")
        search_by_name(search)
    elif search_by == '4':
        add()
    elif search_by == '6':
        search = input("\nInput data ID to be deleted -> ")
        delete(search)
    elif search_by == '7' :
        print("\nThe program has been stopped.")
        print('============================================================')
        loop = False
    else:
        print("\nYour input is invalid.")
        print('============================================================')
        loop = False

    if search_by == '1'  or search_by == '2' or search_by == '3' or search_by == '4' or search_by == '5' or search_by == '6':
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