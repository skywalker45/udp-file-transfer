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

s.setblocking(0)
     
print 'Socket bind complete'
droprate = raw_input('Enter a percentage for the drop rate : ')
droprate = int(droprate)
#now keep talking with the client
# receive data from client (data, addr)
# while True:
# 	d = s.recvfrom(1024)
# 	data = d[0]
# 	addr1 = d[1]
	 
	 
# 	reply = data
	 

# 	print 'Message[' + addr1[0] + ':' + str(addr1[1]) + '] - ' + data.strip()

# 	s.sendto(reply , ("localhost", 8888))

while True:
	# ready = select.select([s], [], [], 1)
	# if ready[0]:
	try:
		d = s.recvfrom(1024)
		reply = d[0]
		addr = d[1]

		print type(reply)

		if reply == "":
			self.kill()

		print "chosing random int"
		x = random.randint(1,100)
		print x

		if not reply == "0":
			if x >= droprate:
				print "passed packet on"
				s.sendto(reply, ("localhost", 8888))
			else:
				print "dropped packet"

	except socket.error , msg:
		pass

s.close()
	
