import socket
import threading
import time

# Semaphores
x = threading.Semaphore(1)
y = threading.Semaphore(1)

readercount = 0

# Reader function
def reader(client_socket):
    global readercount

    # Entry section
    x.acquire()
    readercount += 1
    if readercount == 1:
        y.acquire()
    x.release()

    print(f"\n{readercount} reader is inside")

    time.sleep(5)

    # Exit section
    x.acquire()
    readercount -= 1
    if readercount == 0:
        y.release()
    x.release()

    print(f"\nReader is leaving, remaining: {readercount}")
    client_socket.close()


# Writer function
def writer(client_socket):
    print("\nWriter is trying to enter")
    y.acquire()

    print("\nWriter has entered")
    time.sleep(5)

    y.release()
    print("\nWriter is leaving")
    client_socket.close()


# Main server
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8989))
    server_socket.listen(50)

    print("Listening on port 8989...")

    while True:
        client_socket, addr = server_socket.accept()

        # Receive choice (int)
        data = client_socket.recv(4)
        if not data:
            client_socket.close()
            continue

        choice = int.from_bytes(data, "little")

        if choice == 1:
            t = threading.Thread(target=reader, args=(client_socket,))
            t.start()

        elif choice == 2:
            t = threading.Thread(target=writer, args=(client_socket,))
            t.start()

        else:
            print("Unknown choice received")
            client_socket.close()


if __name__ == "__main__":
    main()
