import socket

ip ='192.168.10.173'
port = 8080 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip, port))
server_socket.listen(1)
client_socket, address = server_socket.accept()

recieved_4 = 0
size_bytes = b''

while recieved_4 <4:
   data = client_socket.recv(4 - recieved_4)
   if not data:    
        break
   size_bytes += data
   recieved_4 += len(data)
if recieved_4 == 4: 
    file_size = int.from_bytes(size_bytes, 'big')
received = 0
with open("received_file.png", "wb") as file:
    while received < file_size:
           data = client_socket.recv(file_size - received)
           if not data:
              break
           file.write(data)
           received += len(data)  
    print(received, file_size)

client_socket.close()
server_socket.close()
print("Server finished")
    




