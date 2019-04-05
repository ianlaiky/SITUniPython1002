import socket
import sys
from thread import *


def connectionStr(con, data, addr):
    try:
        first_line = data.split('\n')[0]
        url = first_line.split(' ')[1]

        http_pos = url.find("://")

        if (http_pos == -1):
            temp = url
        else:
            temp = url[(http_pos + 3):]

        port_pos = temp.find(":")

        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos = len(temp)

        webserver = ""
        port = -1
        if (port_pos == -1 or webserver_pos < port_pos):
            port = 80
            webserver = temp[:webserver_pos]
        else:

            port = int((temp[(port_pos + 1)])[:webserver_pos - port_pos - 1])
            webserver = temp[:port_pos]

        proxy_server(webserver, port, con, addr, data)


    except Exception, e:
        pass


def proxy_server(webserver, port_pos, conn, addr, data):
    try:
        print webserver
        print webserver
        so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        so.connect((webserver, port_pos))
        so.send(data)

        while 1:

            reply = so.recv(4096)
            # print reply
            if (len(reply) > 0):
                conn.sendall(reply)

                dar = float(len(reply))
                dar = float(dar / 1024)
                dar = "%.3s" % (str(dar))
                dar = "%s KB" % (dar)

                print "[*] Requet done : " + str(addr[0]) + " => " + str(dar) + " <="

            else:
                break

        so.close()
        conn.close()
        print "done..."
    except socket.error, (value, message):
        print value
        print message
        so.close()
        # conn.close()
        sys.exit(1)



def start2():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 8081))
        s.listen(5)
        print "Inistaliseng socket"

    except Exception, e:
        print "unable to initisalsie socket"

        sys.exit(2)

    while 1:
        try:
            conn, addr = s.accept()
            data = conn.recv(4096)
            start_new_thread(connectionStr, (conn, data, addr))

        except KeyboardInterrupt:
            s.close()
            sys.exit(1)
    s.close()


start2()
