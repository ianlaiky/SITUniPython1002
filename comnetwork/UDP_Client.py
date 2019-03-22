import socket

msgfromclient = "Hello UDP Server"
bytestosend = str.encode(msgfromclient)
serveraddport = ("192.168.1.10", 20001)
buffersize = 1024

udpclientsocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

udpclientsocket.sendto(bytestosend, serveraddport)

msgfromserver = udpclientsocket.recvfrom(buffersize)

msg = "Message from server {!r}".format(msgfromserver[0])

print (msg)
