import socket

HOST = "192.168.0.154"  # Server IP
PORT = 8080

def main():
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print("Connected to server")

        message = "What are you karing"
        client_socket.sendall(message.encode())
        print("Message sent")

        data = client_socket.recv(1024).decode()
        print("Received from server:", data)

    except Exception as e:
        print("Error:", e)

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
