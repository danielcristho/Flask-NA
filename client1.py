import socket
import sys

# make soket
new_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# localhost
host = 'localhost'
# port 
port = 60
# konek ke server via localhost
server_id = ((host, port))
print("Terhubung")
new_soket.connect(server_id)
# reply ke srv
message = 'message'
new_soket.sendall(message)
# respone
data = new_soket.recv(10)
print(data)
print("Socket closed")
new_soket.close()
