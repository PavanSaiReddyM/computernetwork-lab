import socket

HOST = "192.168.0.255"  # Server IP
PORT = 8080
BUFFER_SIZE = 1024

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((HOST, PORT))
        print("Connected to server. Type messages:")
        
        while True:
            msg = input("> ")
            if msg == "exit":
                break

            sock.sendall(msg.encode())

            data = sock.recv(BUFFER_SIZE)
            if not data:
                print("Server closed connection")
                break

            print("Echo from server:", data.decode())

    except Exception as e:
        print("Error:", e)

    finally:
        sock.close()

if __name__ == "__main__":
    main()
