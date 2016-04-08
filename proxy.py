import socket
import sys
import random

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
droprate = raw_input('Enter a percentage for the drop rate : ') 
#now keep talking with the client
# receive data from client (data, addr)
while True:
	d = s.recvfrom(1024)
	data = d[0]
	addr1 = d[1]
	 
	 
	reply = data
	 

	print 'Message[' + addr1[0] + ':' + str(addr1[1]) + '] - ' + data.strip()
	x = random.randint(1,100)
	print x


	if x < int (droprate):
		s.sendto(reply , ("localhost", 8888))
	else:
		s.sendto('packets dropped' , ("localhost", addr1[1]))
s.close()
	
