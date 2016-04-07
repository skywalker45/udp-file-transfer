import SocketServer
import sys
class MyUDPHandler(SocketServer.BaseRequestHandler):


    def handle(self):
        self.serveraddress = ("localhost", 8989)
        self.client_address = ("localhost", 9999)
        data = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        print data
        print self.client_address[1]
        socket.sendto(data.upper(), (self.serveraddress))

        server2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server2.serve_forever()
        print 'sending back to client now'
        data2 = self.request[0].strip()
        socket2 = self.request[1]
        print "{} wrote:".format(self.serveraddress[0])
        print data2
        print 'while loop'
        print self.serveraddress[1]
        socket.sendto(data2.upper(), (self.client_address))

    def reply(self):
        self.client_address = ("localhost", 9999)
        server2 = SocketServer.UDPServer("localhost", 8989)
        data2 = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote: ".format(server2[0])
        print data
        socket.sendto(data.upper(), self.serveraddress)
        server.close()
        sys.exit()


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    HOST2, PORT2 = "localhost", 8989
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
