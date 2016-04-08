
import socket
import sys
import os
import ast
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
client_address = 'localhost', 9999
# Datagram (udp) socket
try :
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket created'
except socket.error, msg :
	print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
 
 
# Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	 
print 'Socket bind complete'

packets = []
pktNum = 0
file = None
running = 1

def writeFileFromPackets():

	global pktNum

	for x in packets:
		if x[0] == pktNum and pktNum == 0:

			global file
			file = open("Uploads/" + str(x[1]), "a+")
			file.write(str(x[2]))
			pktNum += 1

		elif x[0] == pktNum:
			
			file.write(str(x[2]))
			pktNum += 1

		elif x[3] < pktNum:
			global file
			file.close()
			global running
			running = 0


def storePacket(pkt):
	packets.append(pkt)
	writeFileFromPackets()

while running:

	# receive data from client (data, addr)
	d = s.recvfrom(1024)
	data = d[0]
	addr = d[1]

	if not data:
		break

	packet = ast.literal_eval(data)
	s.sendto(packet[0], (client_address))
	storePacket(packet)
	print packet
	 
s.close()