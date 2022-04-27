from socket import AF_INET, SOCK_STREAM, socket


server_port = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', server_port))
serverSocket.listen(1)
while True:
    connetSocket, ipAdd = serverSocket.accept()
    meg = connetSocket.recv(2048)
    modifiedMeg = meg.decode().upper()
    connetSocket.send(modifiedMeg.encode())
    connetSocket.close()