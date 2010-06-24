import DictProto

socket = DictProto.Socket(DictProto.CLIENT_SOCK, 3020, "localhost")

data = {"CMD": "VER_REQ"}
socket.Send(data)
returndata = socket.Receive()
print returndata["CMD"], ":", returndata["DATA"]
