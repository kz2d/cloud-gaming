import socket as sock
import sys



class Socket:
    def __init__(self):
        self.socket=sock.socket()
        self.socket.connect(('localhost',9090))


    def get(self):
        data=self.socket.recv(8294533)
        return data


    def close(self):
        self.socket.close()



