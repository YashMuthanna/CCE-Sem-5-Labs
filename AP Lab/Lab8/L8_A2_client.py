import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345

client_socket.connect((host, port))

while True:
    choice = input("Enter your choice (1: Search, 2: Sort, 3: Split, exit: to exit): ")
    
    if choice.lower() == "exit":
        client_socket.send(choice.encode())
        client_socket.close()
        break

    if choice in ["1", "2", "3"]:
        data = input("Enter integers (space-separated): ")
        client_socket.send(f"{choice} {data}".encode())
        response = client_socket.recv(1024).decode()
        print(response)
    else:
        print("Invalid choice. Please enter a valid choice (1, 2, 3, or exit).")
