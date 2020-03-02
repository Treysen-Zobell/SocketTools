
from socket_tools import socket_tools
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 12345))
server_socket.listen(10)
server_socket.settimeout(None)

while True:
    conn, address = server_socket.accept()

    while True:
        data = socket_tools.recv(conn)
        if data != 'disconnect':
            socket_tools.send(conn, data)
            print(data)
        else:
            break
    break
