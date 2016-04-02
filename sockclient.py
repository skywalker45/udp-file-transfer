import socket   #for sockets
import sys  #for exit
 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
host = raw_input('Enter an IP to connect to : ')
port = 8888;
 
while(1) :
    #msg = raw_input('Enter message to send : ')
     
    try :
        #Set the whole string
        #s.sendto(msg, (host, port))

        with open("test.txt", "rb") as fi:
            buf = fi.read(32)
            while (buf):
               s.sendto(buf, (host, port))
               buf = fi.read(32)
         
        # receive data from server (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print 'Server() reply : ' + reply
     
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()