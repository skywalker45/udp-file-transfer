import socket
import sys
import random
import select

HOST = "localhost"   # Symbolic name meaning all available interfaces
SERVERPORT = 8888 # Arbitrary non-privileged port
CLIENTPORT = 9999
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
 
# Bind socket to local host and port
try:
    s.bind((HOST, CLIENTPORT))
    
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'

while True:
	ready = select.select([s], [], [], 1)
	if ready[0]:
		d = s.recvfrom(1024)
		reply = d[0]
		addr = d[1]


		print reply

		if reply == "":
			self.kill()

		if not reply == "0":
			s.sendto(reply, ("localhost", 8888))

s.close()
	
