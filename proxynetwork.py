#client
c_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c_tcp.connect((t_remoteHost, t_remotePort))

#server
s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_tcp.bind(('', u_localPort))
s_tcp.listen(1)

conn, addr = s_tcp.accept()
#-------------------------------------

while True:
    u_data, u_addr = u_sock.recvfrom(4096)
    if u_knownClient is None:
        u_knownClient = u_addr
    if u_addr == u_knownClient:
        u_sock.sendto(u_data, u_knownServer)
    else:
        u_sock.sendto(u_data, u_knownClient)


    data = conn.recv(1024)
    if not data: break
    print "received data:", data
    c_tcp.send(data)  # echo
