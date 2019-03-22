import socket
import sys
from thread import *

def connectionStr(con,data,addr):
    try:
        first_line = data.split('\n')[0]
        url = first_line.split(' ')[1]

        http_pos = url.find("://")

        if(http_pos==-1):
            temp = url
        else:
            temp = url[(http_pos+3):]

        port_pos = temp.find(":")

        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos = len(temp)
        webserver = ""
        port = -1
        if (port_pos==-1 or webserver_pos < port_pos):
            port = 80
            webserver = temp[:webserver_pos]
        else:

            port = int((temp[(port_pos+1)])[:webserver_pos-port_pos-1])
            webserver = temp[:port_pos]
        proxy_server(webserver,port,con,addr,data)


    except Exception, e:
        pass

def proxy_server(webserver,port_pos,conn,addr,data):
    try:
        so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        so.connect((webserver, port_pos))
        so.send(data)
        while 1:
            reply = so.recv(2500000)

            if(len(reply)>0):
                conn.send(reply)

                dar = float(len(reply))
                dar = float(dar/1024)
                dar = "%.3s" % (str(dar))
                dar = "%s KB" % (dar)
                'Print A Cussdfdsfd'
                print "[*] Requet done : %s => %s <=" % (str(addr[0]),str(dar))

            else:

                break
        so.close()
        print "done..."
        conn.close()
    except socket.error, (value, message):
        print value
        print message
        so.close()
        conn.close()
        sys.exit(1)



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 8081)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
# Listen for incoming connections
sock.listen(320)
while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(2500000)

            start_new_thread(connectionStr,(connection,data,client_address))
            # print('received {!r}'.format(data))
            # if data:
            #     print('sending data back to the client')
            #     connection.sendall(data)
            # else:
            #     print('no data from', client_address)
            #     break
    finally:
        # Clean up the connection
        connection.close()

