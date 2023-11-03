import socket

def search_number(numbers, target):
    return target in numbers

def sort_numbers(numbers, ascending=True):
    return sorted(numbers) if ascending else sorted(numbers, reverse=True)

def split_odd_even(numbers):
    odd_numbers = [num for num in numbers if num % 2 == 1]
    even_numbers = [num for num in numbers if num % 2 == 0]
    return odd_numbers, even_numbers

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server listening on {host}:{port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    while True:
        data = client_socket.recv(1024).decode()
        choice, *rest = data.split()

        if choice.lower() == "exit":
            client_socket.close()
            break
        elif choice == "1":
            target = int(rest[0])
            result = search_number(numbers, target)
        elif choice == "2":
            ascending = int(rest[0]) == 1
            result = sort_numbers(numbers, ascending)
        elif choice == "3":
            odd, even = split_odd_even(numbers)
            result = f"Odd: {odd}, Even: {even}"
        else:
            result = "Invalid choice"

        client_socket.send(str(result).encode())
