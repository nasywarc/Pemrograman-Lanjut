import pandas as pd
from tkinter import simpledialog, messagebox

def send_data(client_socket, data):
    client_socket.send(data.encode('utf-8'))

def search_id(client_socket, df):
    search = client_socket.recv(1024).decode('utf-8')
    result_df = df[df['id'].astype(str) == search]
    send_data(client_socket, result_df.to_csv(index=False))

def search_name(client_socket, df):
    search = client_socket.recv(1024).decode('utf-8')
    result_df = df[df['name'].astype(str).str.contains(search, case=False)]
    send_data(client_socket, result_df.to_csv(index=False))

def search_filter(client_socket, df):
    neighborhood_group = client_socket.recv(1024).decode('utf-8')
    neighborhood = client_socket.recv(1024).decode('utf-8')
    filter_price = int(client_socket.recv(1024).decode('utf-8'))

    result_df = df[
        (df['neighbourhood_group'].str.lower() == neighborhood_group.lower()) &
        (df['neighbourhood'].str.lower() == neighborhood.lower()) &
        (df['price'].astype(int) <= filter_price)
    ]

    send_data(client_socket, result_df.to_csv(index=False))

def add_data(client_socket, df):
    entries = ['ID', 'Name', 'Host Name', 'Host ID', 'Neighbourhood Group', 'Neighbourhood', 'Latitude', 'Longitude',
               'Room Type', 'Price', 'Minimum Nights', 'Number of Reviews', 'Last Review', 'Reviews per Month',
               'Calculated Host Listings', 'Availability']

    entry_values = [(entry.lower().replace(' ', '_'), client_socket.recv(1024).decode('utf-8')) for entry in entries]

    new_data = dict(entry_values)
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv("new_york_housing.csv", index=False)
    send_data(client_socket, "Data added successfully")

def update_data(client_socket, df):
    search = client_socket.recv(1024).decode('utf-8')

    if search in df['id'].astype(str).values:
        new_availability = int(client_socket.recv(1024).decode('utf-8'))
        df.loc[df['id'].astype(str) == search, 'availability_365'] = new_availability
        df.to_csv("new_york_housing.csv", index=False)
        send_data(client_socket, f"Availability for ID {search} updated successfully")
    else:
        send_data(client_socket, f"There is no ID that matches '{search}'")

def delete_data(client_socket, df):
    delete_ID = client_socket.recv(1024).decode('utf-8')

    if delete_ID in df['id'].astype(str).values:
        delete_or_no = messagebox.askokcancel('Delete Data', f'Do you want to delete {delete_ID} data?')
        if delete_or_no:
            df = df[df['id'].astype(str) != delete_ID]
            df.to_csv("new_york_housing.csv", index=False)
            send_data(client_socket, f"Data with ID {delete_ID} deleted successfully")
    else:
        send_data(client_socket, f"There is no ID that matches '{delete_ID}'")

def send_help(client_socket):
    help_text = "HELP MENU\n\n" \
                "1. Show data\t\t: Show every data in CSV file.\n" \
                "2. Find data by ID\t\t: Search data by Housing ID.\n" \
                "3. Find data by Name\t: Search data by the name of the housing.\n" \
                "4. Find data by Filter\t: Filter search result based on Neighbourhood Group, Neighbourhood, " \
                "and Price.\n" \
                "5. Add data\t\t: Add new entry to the CSV file.\n" \
                "6. Update data\t\t: Update availability of the housing.\n" \
                "7. Delete data\t\t: Delete entry by id.\n" \
                "9. Exit\t\t\t: Stop the program.\n"

    send_data(client_socket, help_text)
