from tkinter import *
import pandas as pd

def set_button_color(button, color, textcolor):
    show_button.config(bg='SystemButtonFace', fg='Black')
    search_id_button.config(bg='SystemButtonFace', fg='Black')
    search_name_button.config(bg='SystemButtonFace', fg='Black')
    search_filter_button.config(bg='SystemButtonFace', fg='Black')
    add_button.config(bg='SystemButtonFace', fg='Black')
    update_button.config(bg='SystemButtonFace', fg='Black')
    delete_button.config(bg='SystemButtonFace', fg='Black')
    help_button.config(bg='SystemButtonFace', fg='Black')

    button.config(bg=color, fg=textcolor)

def show():
    set_button_color(show_button, '#67B274', '#FFFFFF')
    # Fill this code

def search_id():
    set_button_color(search_id_button, '#67B274', '#FFFFFF')
    search_id_window = Toplevel(window)
    search_id_window.title('Search by ID')
    
    id_label = Label(search_id_window, text='Input ID : ')
    id_label.grid(row=0, column=0)
    id_entry = Entry(search_id_window)
    id_entry.grid(row=0, column=1)
    enter_button = Button(search_id_window, text='Search')
    enter_button.grid(row=0, column=2)
    

def search_name():
    set_button_color(search_name_button, '#67B274', '#FFFFFF')
    search_name_window = Toplevel(window)
    search_name_window.title('Search by ID')
    
    name_label = Label(search_name_window, text='Input Name : ')
    name_label.grid(row=0, column=0)
    name_entry = Entry(search_name_window)
    name_entry.grid(row=0, column=1)
    enter_button = Button(search_name_window, text='Search')
    enter_button.grid(row=0, column=2)

def search_filter():
    set_button_color(search_filter_button, '#67B274', '#FFFFFF')
    # Fill this code

def add():
    set_button_color(add_button, '#67B274', '#FFFFFF')
    # global df
    # new_data = {
    #             'id': add_ID,
    #             'name': add_name,
    #             'host_id': add_host_ID,
    #             'host_name': add_host_name,
    #             'neighbourhood_group': add_neighb_grp,
    #             'neighbourhood': add_neighb,
    #             'latitude': add_latitude,
    #             'longitude': add_longitude,
    #             'room_type': add_room_type,
    #             'price': add_price,
    #             'minimum_nights': add_min_nights,
    #             'number_of_reviews': add_num_of_reviews,
    #             'last_review': add_last_review,
    #             'reviews_per_month': add_rev_per_mon,
    #             'calculated_host_listings': add_calc_host,
    #             'availability_365': add_avail
    #             }
    # df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    # df.to_csv("new_york_housing.csv", index=False)
    # print("\nThe data has been created.")
    
    add_window = Toplevel(window)
    add_window.title('Add data')
    
    add_id_label = Label(add_window, text='Input ID : ')
    add_id_label.grid(row=0, column=0)
    add_id_entry = Entry(add_window)
    add_id_entry.grid(row=0, column=1)
    
    add_name_label = Label(add_window, text='Input Name : ')
    add_name_label.grid(row=1, column=0)
    add_name_entry = Entry(add_window)
    add_name_entry.grid(row=1, column=1)
    
    add_hostid_label = Label(add_window, text='Input Host ID : ')
    add_hostid_label.grid(row=2, column=0)
    add_hostid_entry = Entry(add_window)
    add_hostid_entry.grid(row=2, column=1)
    
    add_host_label = Label(add_window, text='Input Host Name : ')
    add_host_label.grid(row=3, column=0)
    add_host_entry = Entry(add_window)
    add_host_entry.grid(row=3, column=1)
    
    add_nbhgrp_label = Label(add_window, text='Input Neighbourhood Group : ')
    add_nbhgrp_label.grid(row=4, column=0)
    add_nbhgrp_entry = Entry(add_window)
    add_nbhgrp_entry.grid(row=4, column=1)
    
    add_nbh_label = Label(add_window, text='Input Neighbourhood : ')
    add_nbh_label.grid(row=5, column=0)
    add_nbh_entry = Entry(add_window)
    add_nbh_entry.grid(row=5, column=1)
    
    add_latitude_label = Label(add_window, text='Input Latitude : ')
    add_latitude_label.grid(row=6, column=0)
    add_latitude_entry = Entry(add_window)
    add_latitude_entry.grid(row=6, column=1)
    
    add_longitude_label = Label(add_window, text='Input Longitude : ')
    add_longitude_label.grid(row=7, column=0)
    add_longitude_entry = Entry(add_window)
    add_longitude_entry.grid(row=7, column=1)
    
    add_room_label = Label(add_window, text='Input Room Type : ')
    add_room_label.grid(row=8, column=0)
    add_room_entry = Entry(add_window)
    add_room_entry.grid(row=8, column=1)
    
    add_price_label = Label(add_window, text='Input Price : ')
    add_price_label.grid(row=9, column=0)
    add_price_entry = Entry(add_window)
    add_price_entry.grid(row=9, column=1)
    
    add_min_label = Label(add_window, text='Input Minimum Nights : ')
    add_min_label.grid(row=10, column=0)
    add_min_entry = Entry(add_window)
    add_min_entry.grid(row=10, column=1)
    
    add_num_label = Label(add_window, text='Input Number of Reviews : ')
    add_num_label.grid(row=11, column=0)
    add_num_entry = Entry(add_window)
    add_num_entry.grid(row=11, column=1)
    
    add_last_label = Label(add_window, text='Input Last Review : ')
    add_last_label.grid(row=12, column=0)
    add_last_entry = Entry(add_window)
    add_last_entry.grid(row=12, column=1)
    
    add_rev_label = Label(add_window, text='Input Reviews per Month : ')
    add_rev_label.grid(row=13, column=0)
    add_rev_entry = Entry(add_window)
    add_rev_entry.grid(row=13, column=1)
    
    add_cal_label = Label(add_window, text='Input Calculated Host Listing : ')
    add_cal_label.grid(row=14, column=0)
    add_cal_entry = Entry(add_window)
    add_cal_entry.grid(row=14, column=1)
    
    add_avail_label = Label(add_window, text='Input Avaibility : ')
    add_avail_label.grid(row=15, column=0)
    add_avail_entry = Entry(add_window)
    add_avail_entry.grid(row=15, column=1)
    
    space_label = Label(add_window, text='')
    space_label.grid(row=16, column=1)
    
    def confirm_add():
        # Retrieve values from entry fields
        add_ID = int(add_id_entry.get())
        add_name = add_name_entry.get()
        add_host_ID = int(add_hostid_entry.get())
        add_host_name = add_host_entry.get()
        add_neighb_grp = add_nbhgrp_entry.get()
        add_neighb = add_nbh_entry.get()
        add_latitude = float(add_latitude_entry.get())
        add_longitude = float(add_longitude_entry.get())
        add_room_type = add_room_entry.get()
        add_price = float(add_price_entry.get())
        add_min_nights = int(add_min_entry.get())
        add_num_of_reviews = int(add_num_entry.get())
        add_last_review = add_last_entry.get()
        add_rev_per_mon = float(add_rev_entry.get())
        add_calc_host = int(add_cal_entry.get())
        add_avail = int(add_avail_entry.get())

        # Create a new data dictionary
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

        # Add the new data to the DataFrame
        global df
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_csv("new_york_housing.csv", index=False)
        print("\nThe data has been created.")

        # Close the Add data window
        add_window.destroy()

    # Create the Add data window
    add_window = Toplevel(window)
    add_window.title('Add data')

    # (Your existing code for creating entry fields)

    confirm_button = Button(add_window, text='Confirm', command=confirm_add)
    confirm_button.grid(row=17, column=1)

def update():
    set_button_color(update_button, '#67B274', '#FFFFFF')
    # Fill this code

def delete():
    set_button_color(delete_button, '#67B274', '#FFFFFF')
    # Fill this code

def help():
    set_button_color(help_button, '#67B274', '#FFFFFF')
    # Fill this code

    help_window = Toplevel(window)
    help_window.title('Help Menu')

    help_text = "\t\t\t\t\tHELP MENU\n\n" \
                "1. Show data\t\t: Show every data in CSV file.\n" \
                "2. Find data by ID\t\t: Search data by Housing ID.\n" \
                "3. Find data by Name\t: Search data by the name of the housing.\n" \
                "4. Find data by Filter\t: Filter search result based on Neighbourhood Group, Neighbourhood, " \
                "and Price.\n" \
                "5. Add data\t\t: Add new entry to the CSV file.\n" \
                "6. Update data\t\t: Update availability of the housing.\n" \
                "7. Delete data\t\t: Delete entry by id.\n" \
                "9. Exit\t\t\t: Stop the program.\n" \

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
add_button = Button(text='Add data', command=add)
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