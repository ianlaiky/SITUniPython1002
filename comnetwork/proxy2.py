#!/usr/bin/python
# Usage: ./net.py
# Description: Proof-of-concept HTTPS proxy script to hide the domain name in a TLS connection
#              so that firewalling appliances can't see who you are trying to connect to.
# Example setup: Edit ../hosts to include "127.0.0.1 imgur.com"
# Browser: http://imgur.com
#          -> TCP 127.0.0.1 80 (Python is listening & reads headers "GET / && Host imgur.com")
#          -> UDP 4.2.2.1 53 (Python performs DNS query on "imgur.com" [non-hosts file lookup])
#          -> TCP 1.2.3.4 443 (Python connects to TLS server & sends headers over encrypted channel [non-cert verify])
#          -> HTTPS response data is proxied back to browser localhost connection
# Warning: This script is very slow and insecure

import re
import socket
import ssl
import subprocess
import SocketServer

resolv = {}


class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        global resolv

        heads = self.request.recv(10024).strip().split("\n")

        page = "";
        host = ""
        for head in heads:
            match = re.match("^get ([^ ]+).*$", head.strip(), re.I)
            if (match):
                page = match.group(1)
            match = re.match("^host: ([^ ]+).*$", head.strip(), re.I)
            if (match):
                host = match.group(1)

        if ((not page) or (not host)):
            print("err", heads)
        else:
            addr = ""
            if (host in resolv.keys()):
                addr = resolv[host]
            else:
                looks = subprocess.check_output(["nslookup", host]).split("\n")
                for look in looks:
                    match = re.match("^address:[ ]+([^ ]+).*$", look.strip(), re.I)
                    if (match):
                        addr = match.group(1)
                resolv[host] = addr

            print(page, host, addr)

            context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            context.verify_mode = ssl.CERT_NONE
            context.check_hostname = False
            conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=addr)
            conn.connect((addr, 443))
            conn.sendall("GET " + page + " HTTP/1.1\r\n" + "Host: " + host + "\r\n" + "Connection: close\r\n" + "\r\n")

            resp = ""
            while (1):
                temp = conn.recv(10024)
                if (not temp):
                    break
                resp += temp
                print temp
            self.request.sendall(resp)


if (__name__ == "__main__"):
    (HOST, PORT) = ("127.0.0.1", 80)
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
