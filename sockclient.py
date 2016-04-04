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

fileaccepted = True                             #we assume the filename is accepted unless told otherwise by the server
s.sendto(":FILENAME:", (host, port))            #indicate that filename will be coming next to server
filename = raw_input('Enter name of File: ')
s.sendto(filename, (host, port))                #send proposed filename to server

d = s.recvfrom(1024)
reply = d[0]
addr = d[1]

if reply == "ERROR: EXISTING FILENAME":
    fileaccepted == False

while not fileaccepted:
    filename = raw_input('That file name already exists!\nPlease provide another filename: ')
    s.sendto(filename, (host, port))                #send proposed filename to server

    d = s.recvfrom(1024)
    reply = d[0]
    addr = d[1]

    if reply != "ERROR: EXISTING FILENAME":
        fileaccepted == True

'''
try :
    #http://stackoverflow.com/questions/25465792/python-binary-eof
    with open(filename, "rb") as infile:
        while True:
            data = infile.read(32)

            if not data:
                break

            s.sendto(data, (host, port))
            
            # receive data from server (data, addr)
            receive()
            
            print 'Server' + str(addr) + ' reply : ' + reply

    s.sendto(":END:", (host, port))
 
except socket.error, msg:
    print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
'''





