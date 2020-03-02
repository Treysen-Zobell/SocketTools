
from socket_tools import socket_tools
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect(('127.0.0.1', 12345))

socket_tools.send(server_socket, None)
print(socket_tools.recv(server_socket))

socket_tools.send(server_socket, True)
print(socket_tools.recv(server_socket))

socket_tools.send(server_socket, 111)
print(socket_tools.recv(server_socket))

socket_tools.send(server_socket, 111.0)
print(socket_tools.recv(server_socket))

socket_tools.send(server_socket, 111j)
print(socket_tools.recv(server_socket))

socket_tools.send(server_socket, 'Hello World')
print(socket_tools.recv(server_socket))

socket_tools.send(server_socket, (None, True, 1, 1.0, 'hello', (0, 1), [1, 2], {'a': 1, 'b': 'c'}))
print(socket_tools.recv(server_socket))

socket_tools.send(server_socket, [1, 2])
print(socket_tools.recv(server_socket))

socket_tools.send(server_socket, {'a': 1, 'b': 'c'})
print(socket_tools.recv(server_socket))

socket_tools.send(server_socket, b'Hello World')
print(socket_tools.recv(server_socket))


socket_tools.send(server_socket, 111j)
complex1 = socket_tools.recv(server_socket)

socket_tools.send(server_socket, 111j)
complex2 = socket_tools.recv(server_socket)

socket_tools.send(server_socket, complex1 * complex2)
print(socket_tools.recv(server_socket))


socket_tools.send(server_socket, 'disconnect')
