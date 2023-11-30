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
    # show_data()

# def show_data():
#     show_window = Toplevel(window)
#     show_window.title('Show Data')
#     data_listbox = Listbox(show_window, width=50, height=10)
#     data_listbox.pack(padx=10, pady=10)
#     data = df[['id', 'name', 'neighbourhood_group', 'price']].to_string(index=False)
#     data_listbox.insert(END, data)

# def show_result():
#     show_result_window = Toplevel(window)
#     show_result_window.title('Result')
#     result_label = Label(show_result_window, text="\nResult\n------")
#     result_label.pack(padx=10, pady=10)
#     result_text = df[['id', 'name', 'neighbourhood_group', 'price']].to_string(index=False)
#     result_listbox = Listbox(show_result_window, width=50, height=10)
#     result_listbox.pack(padx=10, pady=10)
#     result_listbox.insert(END, result_text)

def search_id():
    set_button_color(search_id_button, '#67B274', '#FFFFFF')

def search_name():
    set_button_color(search_name_button, '#67B274', '#FFFFFF')

def search_filter():
    set_button_color(search_filter_button, '#67B274', '#FFFFFF')

def add():
    set_button_color(add_button, '#67B274', '#FFFFFF')

def update():
    set_button_color(update_button, '#67B274', '#FFFFFF')

def delete():
    set_button_color(delete_button, '#67B274', '#FFFFFF')

def help():
    set_button_color(help_button, '#67B274', '#FFFFFF')

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
                # "================================ HELP MENU ================================\n\n" \
                # "=========================================================================" \

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