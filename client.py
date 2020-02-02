
from SocketTools import SocketTools

import socket


try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('127.0.0.1', 12345))

    messages = [b'hello there', 'hello there', 12345, 12345.0, 5j, (1, 2, 3, 'a', 'b', 'c', b'a', b'b', b'c'), {'a': 0, 'b': 1}, True]

    SocketTools.send(server_socket, messages[0])
    SocketTools.send(server_socket, messages[0])
    SocketTools.send(server_socket, messages[0])
    SocketTools.send(server_socket, messages[0])

    while True:
        try:
            message = input('Send: ')
            SocketTools.send(server_socket, message)
            if message == 'disconnect':
                break
        except SocketTools.DisconnectError:
            break

    SocketTools.disconnect(server_socket)

except SocketTools.DisconnectError:
    print('Disconnected.')
