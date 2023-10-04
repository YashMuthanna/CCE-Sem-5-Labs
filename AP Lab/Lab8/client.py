import socket


s = socket.socket()

port = 12346

s.connect(('127.0.0.1', port))

string1 = input("Enter string to send to server: ")
s.send(string1.encode())
print("String sent to client")

print("\nResponse received..")
print(s.recv(1024).decode())
s.close()


