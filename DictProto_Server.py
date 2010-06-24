import DictProto
socket = DictProto.Socket(DictProto.SERVER_SOCK, 3020)
socket.Listen()
def returnversion():
    return "Ver 1.0"
def test():
    return "STR"

Commanddict = {
    "VER_REQ" : returnversion,
    "TEST" : test
    }
while 1:
    a = socket.Receive()
    returndata = Commanddict[a["CMD"]]()
    socket.Send({"CMD" : a["CMD"],
                 "DATA": returndata})
