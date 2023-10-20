import os
import csv
import art
import pandas as pd

def print_data() :
    print("\nResult\n------")
    print(df[['id', 'name', 'neighbourhood_group', 'price']].to_string())

def show () :
    global df
    print_data()

def search_by_id (search) :
    global df
    result_df = df[df['id'].astype(str) == search]

    if not result_df.empty:
        print("\nResult\n------")
        print(result_df[['id', 'name', 'neighbourhood_group', 'price']].to_string())
    else:
        print(f"There is no ID such \"{search}\"\n")

def search_by_name (search) :
    global df
    result_df = df[df['name'].astype(str).str.contains(search, case=False)]
    print("\nResult\n------")

    if not result_df.empty:
        print(result_df[['id', 'name', 'neighbourhood_group', 'price']].to_string())
    else:
        print(f"There is no Name such \"{search}\"\n")

def search_by_filter (search) :
    filter_neighbour = input("Enter Neighbourhood -> ")
    filter_price = input("Enter Max Price -> $")

    try :
        filter_price_int = int(filter_price)
    except ValueError :
        print("\nError : Price is not an integer.\n")

    result_df = df[(df['neighbourhood_group'].astype(str) == search.capitalize()) & (df['neighbourhood'].astype(str) == filter_neighbour.capitalize()) & (df['price'].astype(int) <= filter_price_int)]
    print("\nResult\n------")

    if not result_df.empty:
        print(result_df[['id', 'name', 'neighbourhood_group', 'price']].to_string())
    else:    
        print(f"There is no data that meet's all of the criteria.\n")

def is_duplicate(rows, id_to_check):
    for row in rows:
        if id_to_check == row['id']:
            return True
    return False

def add () :
    global df
    print("You're going to add a new data.\n")

    add_ID = input("Enter ID : ")        
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

    df.loc[len(df.index)] = [add_ID,
                             add_name,
                             add_host_ID,
                             add_host_name,
                             add_neighb_grp,
                             add_neighb,
                             add_latitude,
                             add_longtitude,
                             add_room_type,
                             add_price,
                             add_min_nights,
                             add_num_of_reviews,
                             add_last_review,
                             add_rev_per_mon,
                             add_calc_host,
                             add_avail]

    print("\nThe data has been created.")

def delete(search):
    global file_path
    global found
    found = False
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

def update(search):
    global file_path
    global found
    found = False
    with open(file_path, "r", newline='', encoding="cp437", errors='ignore') as read_file:
        rows = list(csv.DictReader(read_file))
        found = False

    for row in rows:
        if search == row['id']:
            found = True
            new_availability = input("Enter new availability : ")
            row['availability_365'] = new_availability

    if found:
        with open(file_path, "w", newline='', encoding="cp437", errors='ignore') as write_file:
            fieldnames = rows[0].keys()
            writer = csv.DictWriter(write_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Data with ID {search} has been updated.\n")
    else:
        print(f"There is no ID such \"{search}\"\n")

def help_menu():
    os.system('cls')
    print(art.logo)
    print("\n========================= HELP MENU ========================")
    print("1. Show data : Show every data in CSV file .")
    print("2. Find data by ID : Search data by Housing ID.")
    print('''3. Find data by Name : Search data by the name 
   of the housing.''')
    print('''4. Find data by Filter : Filter search result based on 
   Neighbourhood Group, Neighbourhood, and Price.''')
    print("5. Add data : Add new entry to the CSV file.")
    print("6. Update data : Update availability of the housing.")
    print("7. Delete data : Delete entry by id.")
    print("9. Exit : Stop the program.")
    print("============================================================")


# file_path = "C:/Users/Nasywa Azizah/data/coding/git remote/Pemrograman-Lanjut/class/uts/testing/csv/new_york_housing.csv"
file_path = "new_york_housing.csv"
df = pd.read_csv('new_york_housing.csv')

os.system('cls')

print('==============================================================================================')
print(art.logo)

found = False
loop = True
run_again = 0

while loop :

    if run_again > 0 :
        os.system('cls')
        print('==============================================================================================')
        print(art.logo)
    print('==============================================================================================')
    search_by = input("1. Show data\n2. Find data by ID\n3. Find data by Name\n4. Find by Filter\n5. Add data\n6. Update data availability\n7. Delete data\n8. Help menu\n9. Exit\nInput (1-9) -> ")

    if search_by == '1' :
        try :
            show()
        except FileNotFoundError:
            print("\nError : Cannot find filepath.\n")

    elif search_by == '2' :
        search = input("\nInput ID -> ")
        try :
            search_by_id(search)
        except FileNotFoundError:
            print("\nError : Cannot find filepath.\n")

    elif search_by == '3' :
        search = input("\nInput Name -> ")
        try :
            search_by_name(search)
        except FileNotFoundError:
            print("\nError : Cannot find filepath.\n")

    elif search_by == '4':
        print("\nAll criteria must be filled.")
        search = input("Enter Neighbourhood Group -> ")
        try :
            search_by_filter(search)
        except FileNotFoundError:
            print("\nError : Cannot find filepath.\n")

    elif search_by == '5':
        try :
            add()
        except FileNotFoundError:
            print("Error : Cannot find filepath.\n")

    elif search_by == '6':
        search = input("\nInput data ID to be updated -> ")
        try :
            update(search)
        except FileNotFoundError:
            print("\nError : Cannot find filepath.\n")

    elif search_by == '7' :
        search = input("\nInput data ID to be deleted -> ")
        try :
            delete(search)
        except FileNotFoundError:
            print("\nError : Cannot find filepath.\n")

    elif search_by == '8':
        help_menu()

    elif search_by == '9':
        print("\nThe program has been stopped.")
        print('==============================================================================================')
        loop = False

    else:
        print("\nYour input is invalid.")
        print('==============================================================================================')
        loop = False

    if search_by == '1'  or search_by == '2' or search_by == '3' or search_by == '4' or search_by == '5' or search_by == '6' or search_by == '7' or search_by == '8':
        keep_run = input("\nDo you want to continue?\nInput (Yes / No) -> ").lower()

        if keep_run == 'yes' :
            run_again += 1

        elif keep_run == 'no'  :
            print("\nThe program has been stopped.")
            print('==============================================================================================')
            loop = False

        else :
            print("\nYour input is invalid.")
            print('==============================================================================================')
            loop = False