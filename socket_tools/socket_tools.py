
import socket
import json


def send(conn, message):
    if message is None:
        message = b'NoneType'
        message_type = b'0'
    elif type(message) is bool:
        message = str(message).encode()
        message_type = b'1'
    elif type(message) is int:
        message = str(message).encode()
        message_type = b'2'
    elif type(message) is float:
        message = str(message).encode()
        message_type = b'3'
    elif type(message) is complex:
        message = str(message).encode()
        message_type = b'4'
    elif type(message) is str:
        message = message.encode()
        message_type = b'5'
    elif type(message) is tuple:
        message = json.dumps(message).encode()
        message_type = b'6'
    elif type(message) is list:
        message = json.dumps(message).encode()
        message_type = b'7'
    elif type(message) is dict:
        message = json.dumps(message).encode()
        message_type = b'8'
    elif type(message) is bytes:
        message_type = b'9'
    else:
        print(message)
        print(type(message))
        print('How did we get here?')
        message = 'ERROR'
        message_type = b'10'

    transmission = str(len(message)).encode() + b':' + message_type + b':' + message
    conn.sendall(transmission)


def recv(conn, timeout=5):
    try:
        conn.settimeout(timeout)

        message_length = b''
        while b':' not in message_length:
            message_length += conn.recv(1)
        message_length = message_length.decode()[:-1]

        message_type = b''
        while b':' not in message_type:
            message_type += conn.recv(1)
        message_type = message_type[:-1]

        message = b''
        while len(message) < int(message_length):
            message += conn.recv(int(message_length) - len(message))

        if message_type == b'0':
            message = None
        elif message_type == b'1':
            message = 'True' in message.decode()
        elif message_type == b'2':
            message = int(message.decode())
        elif message_type == b'3':
            message = float(message.decode())
        elif message_type == b'4':
            message = complex(message.decode())
        elif message_type == b'5':
            message = message.decode()
        elif message_type == b'6':
            message = tuple(json.loads(message.decode()))
        elif message_type == b'7':
            message = json.loads(message.decode())
        elif message_type == b'8':
            message = json.loads(message.decode())
        elif message_type == b'9':
            pass

        return message

    except socket.error as e:
        print(e)
