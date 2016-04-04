import socket
import threading
import SocketServer

LISTENING_PORT = 8888
SENDING_PORT = 1427
OFFICIAL_HOST = ''


print 'Now listening ......................'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((OFFICIAL_HOST, LISTENING_PORT))
print 'Socket bind complete'
d = s.recvfrom(1024)
data = d[0]
addr = d[1]
print "{} message received ...........".format(addr)
SERVER_HOST = addr[0]
x = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
x.bind((SERVER_HOST, SENDING_PORT))
X.sendto(data, (SERVER_HOST,SENDING_PORT))





