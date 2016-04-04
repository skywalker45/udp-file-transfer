
import socket
import sys
import os
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
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

filename = False
datacoming = False 

while 1:

    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]

    if not data:
        break

    if filename:
        # The filename is here.
        # check if the filename exists
        if not os.path.isfile("Uploads/" + data.strip()):
            # if it doesn't exist: open/create that file and get it ready for writing.
            f = open("Uploads/" + data.strip(), "a+")
            filename = False
        else:
            reply = "ERROR: EXISTING FILENAME"
            s.sendto(reply , addr)

    if data == ":FILENAME:":
        # The filename is coming in the next packet.
        # Get ready to receive it.
        filename = True
    
    elif data == ":DATA:":
        datacoming = True

    elif data == ":END:":
        datacoming = False
        break

    if datacoming:
        f.write(data)
     
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
     
s.close()