import socket   #for sockets
import sys  #for exit
import threading
import select
import time

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
		print "[BREAK]"
		sendPackets()
		startTracking()

def package(d):
	global packetNum
	packetNum += 1

	packets.append((packetNum,filename, d))
	index = len(packets)
	trackit(index)

def trackit(num):
	print "tracking packet " + str(num)
	tracking.append(256)

def sendPackets():
	for packet in packets:
		packet = packet + (len(packets),)       # adding total number of packets to packet.
												# This could not be calculated in advance
												# and is guarunteed to be correct if calulated now.
		s.sendto(str(packet), (host, port))

def startTracking():
	#decrement each array by one and resend the corresponding packet when the count reaches 0
	print "startTracking"
	# while 1:
	#     tracking[:] = [x - 1 for x in tracking]
	#     print "decrementing: " + str(tracking[0])
	#     if tracking[0] <= 0:
	#         break

class listen(threading.Thread):
	
	def __init__(self):
		print "Starting listen() thread..."
		threading.Thread.__init__(self)
		self.running = 1

	def run(self):
		while self.running:
			ready = select.select([s], [], [], 1)
			if ready[0]:
				d = s.recvfrom(1024)
				reply = d[0]
				addr = d[1]

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