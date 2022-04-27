
from socket import AF_INET, SOCK_DGRAM, socket

server_port = 12000

socket = socket(AF_INET, SOCK_DGRAM)
socket.bind(('', server_port))
print("The server is ready to receive")
while True:
    meg, ip = socket.recvfrom(2048)
    modifiedMeg = meg.decode().upper()
    socket.sendto(modifiedMeg.encode(), ip)