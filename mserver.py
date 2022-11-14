import socket
import threading

LOCALHOST = "127.0.0.1"
PORT = 1488

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((LOCALHOST, PORT))
print('Server is available!')

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New User: ", clientAddress)

    def run(self):
        msg = ''
        while True:
            data = self.csocket.recv(4096)
            msg = data.decode()
            print(msg)
            if msg == '':
                print('Disconnection...')
                break
            elif msg == 'Кто самая красивая девушка?':
                self.csocket.send(bytes("Лиза Кунец!", "UTF-8"))

while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
