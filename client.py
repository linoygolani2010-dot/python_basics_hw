import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.10.173', 8080))

file_data = b''
with open("new_photo.png", "rb") as file:
    while True:
         data = file.read(1024)
         file_data += data
         if not data:
             break
    file_size = len(file_data)
    client_socket.sendall(file_size.to_bytes(4,'big'))
    client_socket.sendall(file_data)
    


