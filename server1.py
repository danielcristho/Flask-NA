import socket
import sys

# make tcp/ip socket dengan address family
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# localohost
host = '127.0.0.1'
# make port
port = 60
# bindng dari socket ke port
sock.bind((host, port))
# listen the connection
sock.listen(1)
# waiting for connection
print("Wait for the connection")
connection, client = sock.accept()
print(client, "connected")
# data di terima
data = connection.recv(16)
print("Received %s" % data)
if data:
    connection.sendall(data)
else :
    ("no data from", client)
# close connection
connection.close()    

