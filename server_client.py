# Server socket
import socket

server_socket = socket.socket()
server_details = ("127.0.0.1", 1337)
server_socket.bind(server_details)
server_socket.listen(1)
print("Waiting for connection")

while True:
    client_socket, addr = server_socket.accept()
    print("Connection with {}" .format(addr)) # "established.")
    client_message = client_socket.recv(1024).decode()
    echo_message = "Hello, " + client_message
    client_socket.send(echo_message.encode())
    client_socket.close()
  
  
# Client:

import socket

my_socket = socket.socket()
server_details = ("127.0.0.1", 1337)
my_socket.connect(server_details)
print("Connection established")

send_data = input("Write your message here: ")
my_socket.send(send_data.encode())

server_response = my_socket.recv(1024).decode()
print("Server response: {}".format(server_response))
my_socket.close()
