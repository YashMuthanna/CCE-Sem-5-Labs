import socket

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345

client_socket.connect((host, port))

while True:
    user_input = input("Enter a string (or 'stop' to exit): ")
    client_socket.send(user_input.encode())

    if user_input.lower() == "stop":
        break

    response = client_socket.recv(1024).decode()
    print(response)

client_socket.close()
