import SocketServer

class MyUDPHandler(SocketServer.BaseRequestHandler):


    def handle(self):
        self.serveraddress = ("localhost", 8989)
        data = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        print data
        print self.client_address[1]
        socket.sendto(data.upper(), self.serveraddress)
        smth = self.request[0].strip()
        socket2 = self.request[1]
        print "{} wrote:".format(self.serveraddress[0])
        print data
        print self.serveraddress[1]
        socket.sendto(data.upper(), (self.client_address))

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
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()