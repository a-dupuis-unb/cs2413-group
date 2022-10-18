import socket
import sys
import time

new_socket = socket.socket() # socket library constructor to create socket
host_name = socket.gethostname() # socket library function to retrieve hostname
s_ip = socket.gethostbyname(host_name) # retrieves IP address of host
port = 8080 # this port number is usually free 

new_socket.bind((host_name, port)) # bind the host to the port
print("Binding successful!")
print("This is your IP: ", s_ip)

name = input("Enter name: ")
new_socket.listen(1) # the listen() function takes number of connections as argument

conn, add = new_socket.accept() # The first variable which is conn is connected to the socket and the variable ‘add’ is assigned to the IP address of the client.
print("Received connection from ", add[0])
print("Connection established. Connect from: ", add[0])

client = (conn.recv(1024)).decode() # details of incoming connection stored in client variable. Name can be up to 1024 bytes. Decoded on server
print(client + " has connected.") # prints message when connected
conn.send(name.encode()) # server sends host name

while True:
     message = input("ME: ")
     conn.send(message.encode()) # The user enters the message. This is encoded using encode() and then sent across through the socket.
     message = conn.recv(1024) # The incoming message is received using the recv() of the conn object. It can receive up to 1024 bytes of information.
     message = message.decode() # The message is decoded on the server-side using decode().
     print(client, ": ", message)