import socket

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1',8000))
message = input("enter message>")

message = bytes(message,'utf-8')
clientSocket.send(message)

