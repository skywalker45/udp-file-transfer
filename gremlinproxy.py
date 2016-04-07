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
 
#now keep talking with the client
# receive data from client (data, addr)
d = s.recvfrom(1024)
data = d[0]
addr1 = d[1]
 
 
reply = 'from proxy: ' + data
 

print 'Message[' + addr1[0] + ':' + str(addr1[1]) + '] - ' + data.strip()
x = random.randint(1,100)
print x
droprate = raw_input('Enter a percentage for the drop rate : ')



if x < int (droprate):
	s.sendto(reply , ("localhost", 8888))
	# receive data from client (data, addr)
	d = s.recvfrom(1024)
	data = d[0]
	addr = d[1]
	     
	reply = 'Server got ' + data
	print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	print 'sending back to client'
	s.sendto(reply , ("localhost", addr1[1]))
	print addr1[1]
	s.close()
else:
	s.sendto('packets dropped' , ("localhost", addr1[1]))
	s.close()
	
