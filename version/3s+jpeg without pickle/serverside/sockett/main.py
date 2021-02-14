import socket as sock

class Sockett:
    def __init__(self):
        self.socket=sock.socket()
        self.socket.bind(('',9090))
        self.socket.listen(1)
        self.conn, self.addr=self.socket.accept()
        print('connect:',self.addr)

    def send(self,data):
        self.conn.send(data)

    def close(self):
        self.conn.close()