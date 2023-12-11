import tkinter as tk
from tkinter import simpledialog
import socket

class ClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("Client GUI")

        self.label = tk.Label(master, text="Choose an option:")
        self.label.pack()

        self.show_button = tk.Button(master, text="Show data", command=lambda: self.send_request('show'))
        self.show_button.pack()

        self.search_id_button = tk.Button(master, text="Search by ID", command=lambda: self.search_id())
        self.search_id_button.pack()

        self.search_name_button = tk.Button(master, text="Search by Name", command=lambda: self.search_name())
        self.search_name_button.pack()

        self.search_filter_button = tk.Button(master, text="Search by Filter", command=lambda: self.search_filter())
        self.search_filter_button.pack()

        self.add_button = tk.Button(master, text="Add data", command=lambda: self.add_data())
        self.add_button.pack()

        self.update_button = tk.Button(master, text="Update data", command=lambda: self.update_data())
        self.update_button.pack()

        self.delete_button = tk.Button(master, text="Delete data", command=lambda: self.delete_data())
        self.delete_button.pack()

        self.help_button = tk.Button(master, text="Help", command=lambda: self.send_request('help'))
        self.help_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=master.destroy)
        self.exit_button.pack()

    def send_request(self, request):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 12345))
        client_socket.send(request.encode('utf-8'))
        data = client_socket.recv(4096).decode('utf-8')
        self.show_result(data)
        client_socket.close()

    def show_result(self, result):
        result_window = tk.Toplevel(self.master)
        result_window.title('Result')
        result_text = tk.Text(result_window, wrap=tk.WORD)
        result_text.insert(tk.END, result)
        result_text.pack()

    def search_id(self):
        search = simpledialog.askstring("Search by ID", "Enter ID to search:")
        if search is not None:
            self.send_request(f'search_id\n{search}')

    def search_name(self):
        search = simpledialog.askstring("Search by Name", "Enter name to search:")
        if search is not None:
            self.send_request(f'search_name\n{search}')

    def search_filter(self):
        neighborhood_group = simpledialog.askstring("Filter by Neighborhood Group", "Enter Neighborhood Group:")
        neighborhood = simpledialog.askstring("Filter by Neighborhood", "Enter Neighborhood:")
        filter_price = simpledialog.askstring("Filter by Price", "Enter Max Price:")

        if filter_price is not None:
            self.send_request(f'search_filter\n{neighborhood_group}\n{neighborhood}\n{filter_price}')

    def add_data(self):
        entries = ['ID', 'Name', 'Host Name', 'Host ID', 'Neighbourhood Group', 'Neighbourhood', 'Latitude', 'Longitude',
                   'Room Type', 'Price', 'Minimum Nights', 'Number of Reviews', 'Last Review', 'Reviews per Month',
                   'Calculated Host Listings', 'Availability']

        entry_values = [simpledialog.askstring("Add Data", f"Enter {entry}:") for entry in entries]

        data = '\n'.join(entry_values)
        self.send_request(f'add\n{data}')

    def update_data(self):
        search = simpledialog.askstring("Update Data", "Enter ID to update:")
        if search is not None:
            new_availability = simpledialog.askinteger("Update Data", "Enter new availability:")
            if new_availability is not None:
                self.send_request(f'update\n{search}\n{new_availability}')
            else:
                self.show_result("Please enter a valid integer for availability.")

    def delete_data(self):
        delete_ID = simpledialog.askstring("Delete Data", "Enter ID to delete:")
        if delete_ID is not None:
            self.send_request(f'delete\n{delete_ID}')

if __name__ == "__main__":
    root = tk.Tk()
    app = ClientGUI(root)
    root.mainloop()
