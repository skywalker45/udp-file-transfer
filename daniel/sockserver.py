
import socket
import sys
 
HOST = "127.0.0.1"   # Symbolic name meaning all available interfaces
PORT = 8989 # Arbitrary non-privileged port
msg = ""
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
 
#now keep talking with the client
while 1:
    # Establish connection with client.
    print 'I Got the Message'
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
    print addr, data
    if not data: 
        break
     
    reply = 'OK... i got it.'
    s.sendto(reply , addr)
    s.close()
    sys.exit()


