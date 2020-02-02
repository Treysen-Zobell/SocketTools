
from SocketTools import SocketTools

import threading
import socket


# Client Thread
class ClientThread(threading.Thread):
    def __init__(self, client_socket, client_address):
        print('[+] Starting Thread For (%s:%s)' % client_address)
        threading.Thread.__init__(self)
        self.socket = client_socket
        self.address = client_address

    def run(self):
        try:
            while True:
                message, message_type = SocketTools.receive(self.socket, timeout=None)
                print(message, message_type)

        except SocketTools.DisconnectError:
            print('[-] Killing Thread For (%s:%s)' % self.address)
            self.socket.shutdown(2)
            self.socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 12345))
server_socket.listen(5)
server_socket.settimeout(None)

while True:
    conn, address = server_socket.accept()
    client_thread = ClientThread(conn, address)
    client_thread.start()
