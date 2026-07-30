# Python
A basic "Hello World" script.

```python
print("Hello World!")
```

## Sockets
Build a simple tcp/ip connection using the `socket` module.
```python
import socket

#generic socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
```

Creating a Server for use over tcp/ip.
```python
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 80)) #socket.gethostname() is a string, and 80 is the port we want to accept connections on

while True:
    (clientsocket, address) = serversocket.accept()
    print(f"Connection from {address}")
    ct = client_thread(clientsocket)
    ct.run()
```

Creating an object for a client-side tcp/ip connection.
```python
import socket

class ClientSocket:
    def __init__(self, sock=None):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) if sock is None else sock
    
    def connect(self, host:str, port:int):
        self.sock.connect((host, port))
    
    def mysend(self, msg:str):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
    
    def myreceive(self):
        chunks = []
        bytes_recv = 0
        while bytes_recv < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recv, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recv = bytes_recv + len(chunk)
        return b''.join(chunks)
```
