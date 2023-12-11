import socket
import threading
import pandas as pd
from server_functions import *

data_lock = threading.Lock()
df = pd.read_csv('new_york_housing.csv')

def handle_client(client_socket, df):
    request = client_socket.recv(1024).decode('utf-8')

    if request == 'show':
        send_data(client_socket, df.to_csv(index=False))
    elif request == 'search_id':
        search_id(client_socket, df)
    elif request == 'search_name':
        search_name(client_socket, df)
    elif request == 'search_filter':
        search_filter(client_socket, df)
    elif request == 'add':
        add_data(client_socket, df)
    elif request == 'update':
        update_data(client_socket, df)
    elif request == 'delete':
        delete_data(client_socket, df)
    elif request == 'help':
        send_help(client_socket)
    else:
        client_socket.send("Invalid command".encode('utf-8'))

    client_socket.close()

def send_data(client_socket, data):
    client_socket.send(data.encode('utf-8'))

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(5)

    print("Server listening on port 12345")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, df))
        client_handler.start()

if __name__ == "__main__":
    start_server()
