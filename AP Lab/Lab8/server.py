import socket

s = socket.socket()
print ("Socket successfully created")

port = 12346

s.bind(('', port))
print ("socket binded to %s" %(port))

s.listen(5)
print ("socket is listening..")


c, addr = s.accept()
print ('Got connection from', addr )
string1 = c.recv(1024).decode()
print("Receiverd string: ", string1)
if string1 == string1[::-1]:
    c.send("Palindrome".encode())
else:
    c.send("Not a palindrome".encode())
print("Response Sent to client..")
c.close()
s.close()


