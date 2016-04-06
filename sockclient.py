import socket   #for sockets
import sys  #for exit
import threading
import select

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

host = raw_input('Enter an IP to connect to : ')
port = 8888;

filename = ""

packets = []
tracking = []   # this variable will hold a buffer of all the packets and the time that it has been since they left
                # when that time expires it will be sent again

def main():

    filename = raw_input('Enter name of File: ')

    #http://stackoverflow.com/questions/25465792/python-binary-eof
    with open(filename, "rb") as infile:
        while True:
            data = infile.read(32)
            if not data:
                break

            package(data)
        print "[BREAK]"
        listen = False
        print "listen == False"

def package(d):
    print "packaging data:\n\"\n" + d + "\n\""
    packets.append((filename, d))
    index = len(packets)
    trackit(index)

def trackit(num):
    print "tracking packet " + str(num)


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

        print "...listen() stopped."

    def kill(self):
        self.running = 0
        print "Killing listen()..."


if __name__ == '__main__':
    # listen for response from server
    print "doing stuff"
    # t = threading.Thread(target=listen)
    listener = listen()
    listener.start()
    print "running main..."
    main()
    listener.kill()