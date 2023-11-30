from tkinter import *
from tkinter import ttk
from tkinter import simpledialog, messagebox
import pandas as pd
import os
 
def set_button_color(button, color, textcolor):
    for btn in [show_button, search_id_button, search_name_button, search_filter_button,
                add_button, update_button, delete_button, help_button]:
        btn.config(bg='SystemButtonFace', fg='Black')
    button.config(bg=color, fg=textcolor)
    
def show():
    set_button_color(show_button, '#67B274', '#FFFFFF')

    show_window = Toplevel(window)
    show_window.title('New York Housing')

    tree = ttk.Treeview(show_window)
    
    # Menampilkan data dari DataFrame ke dalam Treeview
    tree["columns"] = tuple(df.columns)
    tree.heading("#0", text="Index")
    for col in df.columns:
        tree.heading(col, text=col)
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    
    tree.pack()
 
def show_data():
    show_window = Toplevel(window)
    show_window.title('Show Data')
    data_listbox = Listbox(show_window, width=50, height=10)
    data_listbox.pack(padx=10, pady=10)
    data = df[['id', 'name', 'neighbourhood_group', 'price']].to_string(index=False)
    data_listbox.insert(END, data)
 
def search_id():
    set_button_color(search_id_button, '#67B274', '#FFFFFF')
    search = simpledialog.askstring("Search by ID", "Enter ID to search:")
    if search is not None:
        result_df = df[df['id'].astype(str) == search]
        show_search_results(result_df)
 
def search_name():
    set_button_color(search_name_button, '#67B274', '#FFFFFF')
    search = simpledialog.askstring("Search by Name", "Enter name to search:")
    if search is not None:
        result_df = df[df['name'].astype(str).str.contains(search, case=False)]
        show_search_results(result_df)
 
def show_search_results(result_df):
    result_window = Toplevel(window)
    result_window.title('Search Results')
 
    if result_df.empty:
        result_label = Label(result_window, text=f"No results found.")
        result_label.pack(padx=10, pady=10)
    else:
        result_listbox = Listbox(result_window, width=50, height=10)
        result_listbox.pack(padx=10, pady=10)
 
        for index, row in result_df.iterrows():
            result_listbox.insert(END, f"ID: {row['id']}")
            result_listbox.insert(END, f"Name: {row['name']}")
            result_listbox.insert(END, f"Neighbourhood Group: {row['neighbourhood_group']}")
            result_listbox.insert(END, f"Price: {row['price']}")
            result_listbox.insert(END, f"Availability: {row['availability_365']}")
            result_listbox.insert(END, "-" * 50)  # Separator between housing entries
 
def search_filter():
    set_button_color(search_filter_button, '#67B274', '#FFFFFF')
    
    neighborhood_group = simpledialog.askstring("Filter by Neighborhood Group", "Enter Neighborhood Group:")
    neighborhood = simpledialog.askstring("Filter by Neighborhood", "Enter Neighborhood:")
    
    while True:
        filter_price = simpledialog.askstring("Filter by Price", "Enter Max Price:")
        if filter_price is not None:
            try:
                filter_price_int = int(filter_price)
                break
            except ValueError:
                messagebox.showwarning("Invalid Input", "Please enter a valid integer for price.")
        else:
            return
    
    result_df = df[
        (df['neighbourhood_group'].str.lower() == neighborhood_group.lower()) &
        (df['neighbourhood'].str.lower() == neighborhood.lower()) &
        (df['price'].astype(int) <= filter_price_int)
    ]
    show_search_results(result_df)

     
def add_data_gui():
    global df
    add_data_window = Toplevel(window)
    add_data_window.title("Add Data")
 
    entries = ['ID', 'Name', 'Host Name', 'Host ID', 'Neighbourhood Group', 'Neighbourhood', 'Latitude', 'Longitude',
               'Room Type', 'Price', 'Minimum Nights', 'Number of Reviews', 'Last Review', 'Reviews per Month',
               'Calculated Host Listings', 'Availability']
 
    entry_values = []
    for entry in entries:
        value = simpledialog.askstring("Add Data", f"Enter {entry}:")
        if value is None:
            return
        entry_values.append((entry.lower().replace(' ', '_'), value))
 
    new_data = dict(entry_values)
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv("new_york_housing.csv", index=False)
    messagebox.showinfo("Add Successful", "The data has been added.")
    # show_data()
 
def update():
    set_button_color(update_button, '#67B274', '#FFFFFF')
 
    def update_data():
        search = simpledialog.askstring("Update Data", "Enter ID to update:")
        if search is not None:
            if search in df['id'].astype(str).values:
                new_availability = simpledialog.askinteger("Update Data", "Enter new availability:")
                if new_availability is not None:
                    df.loc[df['id'].astype(str) == search, 'availability_365'] = new_availability
                    df.to_csv("new_york_housing.csv", index=False)
                    messagebox.showinfo("Update Successful", f"Availability for ID {search} updated successfully.")
                    # show_data()
                else:
                    messagebox.showwarning("Invalid Input", "Please enter a valid integer for availability.")
            else:
                messagebox.showwarning("ID not found", f"There is no ID that matches '{search}'.")
 
    update_data()
 
def delete():
    set_button_color(delete_button, '#67B274', '#FFFFFF')
    global df

    delete_ID = simpledialog.askstring("Delete Data", "Enter ID to delete:")

    if delete_ID is not None:
        if delete_ID in df['id'].astype(str).values:
            df = df[df['id'].astype(str) != delete_ID]
            df.to_csv("new_york_housing.csv", index=False)
            messagebox.showinfo("Delete Successful", f"Data with ID {delete_ID} deleted successfully.")
        else:
            messagebox.showwarning("ID not found", f"There is no ID that matches '{delete_ID}'.")

 
def help():
    set_button_color(help_button, '#67B274', '#FFFFFF')
 
    help_window = Toplevel(window)
    help_window.title('Help Menu')
 
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
 
    help_label = Label(help_window, text=help_text, justify=LEFT)
    help_label.pack(padx=10, pady=10)
 
df = pd.read_csv('new_york_housing.csv')
 
window = Tk()
window.title('New York Housing')
window.config(padx=50, pady=30)
window.minsize(width=300, height=200)

title_label = Label(text='New York Housing', width=30)
title_label.grid(row=0, column=0, columnspan=3)
space_1 = Label(text='')
space_1.grid(row=1, column=1)
space_2 = Label(text='')
space_2.grid(row=3, column=1)
space_3 = Label(text='')
space_3.grid(row=5, column=1)
space_4 = Label(text='')
space_4.grid(row=7, column=1)
space_5 = Label(text='')
space_5.grid(row=9, column=1)
space_6 = Label(text='')
space_6.grid(row=11, column=1)
space_7 = Label(text='')
space_7.grid(row=13, column=1)
space_8 = Label(text='')
space_8.grid(row=15, column=1)
space_9 = Label(text='')
space_9.grid(row=17, column=1)


show_button = Button(text='Show', command=show)
show_button.grid(row=2, column=1)
search_id_button = Button(text='Search by ID', command=search_id)
search_id_button.grid(row=4, column=1)
search_name_button = Button(text='Search by Name', command=search_name)
search_name_button.grid(row=6, column=1)
search_filter_button = Button(text='Search by Filter', command=search_filter)
search_filter_button.grid(row=8, column=1)
add_button = Button(text='Add data', command=add_data_gui)
add_button.grid(row=10, column=1)
update_button = Button(text='Update data', command=update)
update_button.grid(row=12, column=1)
delete_button = Button(text='Delete data', command=delete)
delete_button.grid(row=14, column=1)
help_button = Button(text='Help', command=help)
help_button.grid(row=16, column=1)
exit_button = Button(text='Exit', command=exit)
exit_button.grid(row=18, column=1)
 
window.mainloop()