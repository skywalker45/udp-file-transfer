import socket   #for sockets
import sys  #for exit
import threading
import select
import time
import multiprocessing

# create dgram udp socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print 'Failed to create socket'
	sys.exit()

host = raw_input('Enter an IP to connect to : ')
port = 9999;

filename = ""

packetNum = -1
packets = []
tracking = []   # this variable will keep track of the time that
				# has passed since each packet left. When that time
				# expires it will be sent again.

def main():
	global filename
	filename = raw_input('Enter name of File: ')

	#http://stackoverflow.com/questions/25465792/python-binary-eof
	with open(filename, "rb") as infile:
		while True:
			data = infile.read(32)
			if not data:
				break
			package(data)
		appendSize()
		sendPackets()

def appendSize():

	global packets

	for x in xrange(0,len(packets)):
		packets[x] = packets[x] + (len(packets),)


def package(d):
	global packetNum
	packetNum += 1
	packets.append((packetNum,filename, d))
	tracking.append(True)


def sendPackets():
	for packet in packets:
		packet = packet + (len(packets),)       # adding total number of packets to packet.
												# This could not be calculated in advance
												# and is guarunteed to be correct if calulated now.
		trackit(packet[0])
		# s.sendto(str(packet), (host, port))
		

def trackit(pktNum):
	
	print "sending packet " + str(pktNum)
	
	s.sendto(str(packets[pktNum]), (host, port))	
	time.sleep(0.1)
	
	while tracking[pktNum]:
		for x in xrange(1,10):
			time.sleep(0.1)
		print "sending packet " + str(pktNum) + " again..."


class listen(threading.Thread):
	
	def __init__(self):
		print "Starting listen() thread..."
		threading.Thread.__init__(self)
		self.running = 1

	def run(self):
		while self.running:
			global tracking
			ready = select.select([s], [], [], 1)
			if ready[0]:
				d = s.recvfrom(1024)
				reply = d[0]
				addr = d[1]

				tracking[int(reply)] = False

				print reply

				if reply == "":
					self.kill()

		print "...listen() stopped."

	def kill(self):
		self.running = 0
		print "Killing listen()..."


if __name__ == '__main__':

	listener = listen()
	listener.start()            # listen for response from server
	
	main()
	time.sleep(5)
	listener.kill()             # kill listener in case it's still running
