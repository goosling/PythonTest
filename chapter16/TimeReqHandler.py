__author__ = 'joe'
# !/usr/bin/env python
# -*-coding:utf-8-*-

from SocketServer import ThreadingMixIn as TMI, TCPServer, StreamRequestHandler as SRH
import time

class TimeRequestHandler(SRH):
    def handle(self):
        req = self.rfile.readline().strip()
        if req == 'asctime':
            result = time.asctime()
        elif req == "seconds":
            result = str(int(time.time()))
        elif req == 'rfc822':
            result = time.strftime('%a, %d %b %Y %H:%M:%S +0000', time.gmtime())
        else:
            result = """"""

        self.wfile.write(result + "\n")

class TimeServer(TMI, TCPServer):
    allow_reuse_address = 1

serveraddr = ('', 8765)
srvr = TimeServer(serveraddr, TimeRequestHandler)
srvr.serve_forever()