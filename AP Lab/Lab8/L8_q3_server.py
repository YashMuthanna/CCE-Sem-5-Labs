import socket

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return {v: s.count(v) for v in vowels}

# Set up the server socket
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

        if data.lower() == "stop":
            client_socket.close()
            break

        palindrome_result = is_palindrome(data)
        vowels_count = count_vowels(data)

        response = f"Is Palindrome: {palindrome_result}\n"
        response += f"String Length: {len(data)}\n"
        response += "Vowel Counts:\n"
        for vowel, count in vowels_count.items():
            response += f"{vowel}: {count}\n"

        client_socket.send(response.encode())

server_socket.close()
