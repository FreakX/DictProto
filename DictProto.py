import socket
import pickle


SERVER_SOCK = 0x00
CLIENT_SOCK = 0x01

class Socket(object):
    def __init__(self, socktype, port, host=""):
        if socktype == SERVER_SOCK:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind(('', port))
        elif socktype == CLIENT_SOCK:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((host, port))
        self.socktype = socktype
        self.port = port
        self.protoverstr = "DictProto_v1.2"
    def __del__(self):
        if self.socktype == ClIENT_SOCK:
            try:
                self.socket.send("E:E")
            except: pass
            try:
                self.socket.close()
            except: pass
        if self.socktype == SERVER_SOCK:
            try:
                self.conn.send("E:E")
            except: pass
            try:
                self.conn.close()
            except: pass
    def Listen(self):
        self.socket.listen(1)
        self.conn, addr = self.socket.accept()
    

        
    def Send(self, datadict):
        packet = self.protoverstr + pickle.dumps(datadict)
        if self.socktype == CLIENT_SOCK: self.socket.send(packet)
        if self.socktype == SERVER_SOCK: self.conn.send(packet)
        
    def Receive(self):
        while True:
            if self.socktype == SERVER_SOCK: data = self.conn.recv(4096)
            if self.socktype == CLIENT_SOCK: data = self.socket.recv(4096)
            if self.protoverstr in data:
                data = data.split(self.protoverstr)[1]
                returndict = pickle.loads(data)
                return returndict
            if data == "E:E":
                self.__del__()
                    
                
