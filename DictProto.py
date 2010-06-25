import socket


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
        self.protoverstr = "DictProto_v1.1"
    def __del__(self):
        self.socket.close()
    def Listen(self):
        self.socket.listen(1)
        self.conn, addr = self.socket.accept()
    

        
    def Send(self, datadict):
        packet = []
        packet.append(self.protoverstr)
        for x in datadict:
            keylen = hex(len(str(x)))[2:]
            if len(keylen) == 1:
                packet.append("0")
                packet.append(keylen)
            else:
                packet.append(keylen)
                
            key = str(x)
            packet.append(key)
            
            datalen = hex(len(str(datadict[x])))[2:]
            if len(datalen) == 1:
                packet.append("00")
                packet.append(datalen)
            elif len(datalen) == 2:
                packet.append("0")
                packet.append(datalen)
            else:
                packet.append(datalen)
                
            data = str(datadict[x])
            packet.append(data)
            
        if self.socktype == CLIENT_SOCK: self.socket.send(''.join(packet))
        if self.socktype == SERVER_SOCK: self.conn.send(''.join(packet))
        
    def Receive(self):
        while True:
            if self.socktype == SERVER_SOCK: data = self.conn.recv(4096)
            if self.socktype == CLIENT_SOCK: data = self.socket.recv(4096)
            if self.protoverstr in data:
                data = data.split(self.protoverstr)[1]
                returndict = {}
                offset = 0
                while True:
                    try:
                        keylen = int(data[offset:offset+2], 16)
                        offset +=2
                        key = data[offset:offset+keylen]
                        offset +=keylen
                        datalen = int(data[offset:offset+3], 16)
                        offset +=3
                        pdata = data[offset:offset+datalen]
                        offset +=datalen


                        
                        returndict[key] = pdata

                    except:
                        break
                return returndict
                    
                
