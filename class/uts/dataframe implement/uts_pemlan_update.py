import tkinter as tk
from tkinter import messagebox
import socket
import threading
import pandas as pd

class HousingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Housing Data Management")
        
        # GUI Components
        self.label = tk.Label(master, text="Select an action:")
        self.label.pack()

        self.show_button = tk.Button(master, text="Show Data", command=self.show_data)
        self.show_button.pack()

        self.find_id_button = tk.Button(master, text="Find Data by ID", command=self.find_data_by_id)
        self.find_id_button.pack()

        self.find_name_button = tk.Button(master, text="Find Data by Name", command=self.find_data_by_name)
        self.find_name_button.pack()

        self.find_filter_button = tk.Button(master, text="Find Data by Filter", command=self.find_data_by_filter)
        self.find_filter_button.pack()

        self.add_button = tk.Button(master, text="Add Data", command=self.add_data)
        self.add_button.pack()

        self.update_button = tk.Button(master, text="Update Data Availability", command=self.update_data)
        self.update_button.pack()

        self.delete_button = tk.Button(master, text="Delete Data", command=self.delete_data)
        self.delete_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=self.master.destroy)
        self.exit_button.pack()

        # Networking
        self.server_thread = threading.Thread(target=self.start_server)
        self.server_thread.start()

    def start_server(self):
        # Start the server on a separate thread
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 12345))  # Use any available port
        server_socket.listen(5)

        while True:
            client_socket, addr = server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        # Handle communication with a client
        try:
            data = client_socket.recv(1024).decode()
            if data == 'show':
                result = self.get_data_as_string()
                client_socket.send(result.encode())
            elif data.startswith('find_by_id'):
                _, search_id = data.split(',')
                result = self.search_by_id(search_id)
                client_socket.send(result.encode())
            # Add similar handling for other actions (find_by_name, find_by_filter, add, update, delete)
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client_socket.close()

    def show_data(self):
        # Send request to server to get data
        self.send_request('show')

    def find_data_by_id(self):
        search_id = tk.simpledialog.askstring("Find Data by ID", "Enter ID:")
        if search_id:
            self.send_request(f'find_by_id,{search_id}')

    def find_data_by_name(self):
        search_name = tk.simpledialog.askstring("Find Data by Name", "Enter Name:")
        if search_name:
            self.send_request(f'find_by_name,{search_name}')

    def find_data_by_filter(self):
        # Implement similar logic for finding by filter
        pass

    def add_data(self):
        # Implement logic for adding data
        pass

    def update_data(self):
        search_id = tk.simpledialog.askstring("Update Data Availability", "Enter ID:")
        if search_id:
            new_availability = tk.simpledialog.askinteger("Update Data Availability", "Enter new availability:")
            if new_availability is not None:
                self.send_request(f'update,{search_id},{new_availability}')

    def delete_data(self):
        search_id = tk.simpledialog.askstring("Delete Data", "Enter ID:")
        if search_id:
            self.send_request(f'delete,{search_id}')

    def send_request(self, message):
        # Send request to the server and get the response
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 12345))  # Connect to the server
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        client_socket.close()

        # Process the response
        if message == 'show':
            self.display_data(response)
        elif message.startswith('find_by_id'):
            self.display_data(response)
        # Add similar processing for other actions (find_by_name, find_by_filter, add, update, delete)

    def display_data(self, data):
        # Display the data using tkinter messagebox or any other GUI component
        messagebox.showinfo("Result", data)

    def get_data_as_string(self):
        # Return the entire data as a string (for 'show' action)
        return df.to_string(index=False)

    def search_by_id(self, search_id):
        # Implement logic for searching by ID and return the result as a string
        pass

# Load DataFrame from CSV
file_path = "new_york_housing.csv"
df = pd.read_csv(file_path)

# Create and run the GUI
root = tk.Tk()
app = HousingApp(root)
root.mainloop()
