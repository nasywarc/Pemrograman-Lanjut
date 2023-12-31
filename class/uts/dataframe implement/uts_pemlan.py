import os
import art
import pandas as pd

def print_data (data_by, condition, result, unique) :
    print("\nResult\n------")
    if not condition:
        print(result[['id', 'name', 'neighbourhood_group', 'price']].to_string())
    else:
        print(f"\nThere is no {data_by} that {unique}")
    print(line)

def show () :
    print("\nResult\n------")
    print(df[['id', 'name', 'neighbourhood_group', 'price']].to_string())

def search_by_id (search) :
    result_df = df[df['id'].astype(str) == search]
    print_data(data_by="ID", condition=result_df.empty, result=result_df, unique=f'like \"{search}\"')

def search_by_name (search) :
    result_df = df[df['name'].astype(str).str.contains(search, case=False)]
    print_data(data_by="name", condition=result_df.empty, result=result_df, unique=f'like \"{search}\"')

def search_by_filter(search):
    price_check = False
    filter_neighbour = input("Enter Neighbourhood -> ")

    while price_check != True :
        try:
            filter_price = input("Enter Max Price -> $")
            filter_price_int = int(filter_price)
            price_check = True
        except ValueError:
            print("\nError: Price is not an integer.")
    
    result_df = df[(df['neighbourhood_group'].str.lower() == search.lower()) & (df['neighbourhood'].str.lower() == filter_neighbour.lower()) & (df['price'].astype(int) <= filter_price_int)]
    print_data(data_by="data", condition=result_df.empty, result=result_df, unique='meets all of the criteria.')

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
    add_longitude = input("Enter longitude : ")
    add_room_type = input("Enter room type : ")
    add_price = input("Enter price : ")
    add_min_nights = input("Enter minimum nights : ")
    add_num_of_reviews = input("Enter number of reviews : ")
    add_last_review = input("Enter last review : ")
    add_rev_per_mon = input("Enter reviews per month : ")
    add_calc_host = input("Enter calculated host listing count : ")
    add_avail = input("Enter availability : ")

    new_data = {
                'id': add_ID,
                'name': add_name,
                'host_id': add_host_ID,
                'host_name': add_host_name,
                'neighbourhood_group': add_neighb_grp,
                'neighbourhood': add_neighb,
                'latitude': add_latitude,
                'longitude': add_longitude,
                'room_type': add_room_type,
                'price': add_price,
                'minimum_nights': add_min_nights,
                'number_of_reviews': add_num_of_reviews,
                'last_review': add_last_review,
                'reviews_per_month': add_rev_per_mon,
                'calculated_host_listings': add_calc_host,
                'availability_365': add_avail
                }
    
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv("new_york_housing.csv", index=False)
    print("\nThe data has been created.")

def update(search):
    global df
    if search in df['id'].astype(str).values:
        new_availability = input("Enter new availability: ")
        try :
            new_availability_int = int(new_availability)
            df.loc[df['id'].astype(str) == search, 'availability_365'] = new_availability_int
            df.to_csv("new_york_housing.csv", index=False)
            print(f"\nAvailability for ID \"{search}\" updated successfully.")
        except ValueError :
            print("\nError : Please input an integer.")
    else:
        print(f"There is no ID that like \"{search}\"")

def delete():
    global df
    print("You're going to delete a data by ID.\n")
    delete_ID = input("Enter ID to delete: ")

    if delete_ID in df['id'].astype(str).values:
        df = df[df['id'].astype(str) != delete_ID]
        df.to_csv("new_york_housing.csv", index=False)
        print(f"Data with ID {delete_ID} deleted successfully.")
    else:
        print(f"There is no ID that like \"{delete_ID}\"")

def help_menu():
    os.system('cls')
    print(line)
    print(art.logo)
    print("======================================== HELP MENU ===========================================")
    print("1. Show data\t\t: Show every data in CSV file .")
    print("2. Find data by ID\t: Search data by Housing ID.")
    print("3. Find data by Name\t: Search data by the name of the housing.")
    print('''4. Find data by Filter\t: Filter search result based on Neighbourhood Group, Neighbourhood, 
   and Price.''')
    print("5. Add data\t\t: Add new entry to the CSV file.")
    print("6. Update data\t\t: Update availability of the housing.")
    print("7. Delete data\t\t: Delete entry by id.")
    print("9. Exit\t\t\t: Stop the program.")
    print(line)


file_path = "new_york_housing.csv"
df = pd.read_csv('new_york_housing.csv')

line = '=============================================================================================='
os.system('cls')
print(line)
print(art.logo)
loop = True

while loop :

    os.system('cls')
    print(line)
    print(art.logo)
    print(line)
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
        try :
            delete()
        except FileNotFoundError:
            print("\nError : Cannot find filepath.\n")

    elif search_by == '8':
        help_menu()

    elif search_by == '9':
        print('\n====================================== EXITING PROGRAM =======================================')
        loop = False

    else:
        print("\nYour input is invalid.")
        print(line)
        loop = False

    if search_by == '1'  or search_by == '2' or search_by == '3' or search_by == '4' or search_by == '5' or search_by == '6' or search_by == '7' or search_by == '8':
        keep_run = input("\nDo you want to continue?\nInput (Yes / No) -> ").lower()

        if keep_run == 'no'  :
            print("\nThe program has stopped.\n")
            loop = False

        elif keep_run == 'yes' :
            loop = True

        else :
            print("\nYour input is invalid.")
            loop = False