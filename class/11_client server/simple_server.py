import socket

def start_server():
    # Inisialisasi socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding socket ke alamat dan port tertentu
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Mendengarkan koneksi
    server_socket.listen(1)
    print(f"Server mendengarkan di {server_address}")

    while True:
        # Menunggu koneksi dari client
        print("Menunggu koneksi...")
        client_socket, client_address = server_socket.accept()
        print(f"Koneksi diterima dari {client_address}")

        # Menerima data dari client
        data = client_socket.recv(1024)
        print(f"Data diterima: {data.decode()}")

        # Mengirim balasan ke client
        message = "Pesan diterima. Terima kasih!"
        client_socket.sendall(message.encode())

        # Menutup koneksi dengan client
        client_socket.close()

if __name__ == "__main__":
    start_server()
