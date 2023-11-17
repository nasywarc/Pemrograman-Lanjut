import socket

def start_client():
    # Inisialisasi socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Menghubungkan ke server
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)
    
    # Mengirim pesan ke server
    message = "Halo, ini pesan dari client!"
    client_socket.sendall(message.encode())

    # Menerima balasan dari server
    data = client_socket.recv(1024)
    print(f"Balasan dari server: {data.decode()}")

    # Menutup koneksi dengan server
    client_socket.close()

if __name__ == "__main__":
    start_client()
