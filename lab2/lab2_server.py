import socket

HOST = "0.0.0.0"  # Bind to all interfaces
PORT = 8080

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow port reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    server_socket.listen(3)

    print(f"Server listening on port {PORT}...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024).decode()
    print("Received from client:", data)

    response = "what are you karing"
    conn.sendall(response.encode())
    print("Reply sent")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()
