import socket

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverSocket.bind(('',8000))
print("..................waiting for connection...................")
serverSocket.listen(5)
while True:
    (clientSocket,addr) = serverSocket.accept()
    print(addr[0] + " connected")
    message = clientSocket.recv((2048))
    print(message.decode())

