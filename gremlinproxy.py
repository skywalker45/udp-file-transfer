import SocketServer

class MyUDPHandler(SocketServer.BaseRequestHandler):


    def handle(self):
        
        self.serveraddress = ("localhost", 8989)
        data = self.request[0].strip()
        socket = self.request[1]

        socket.sendto(data, self.serveraddress)
        smth = self.request[0].strip()
        socket2 = self.request[1]
        
        socket.sendto(data, (self.client_address))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()