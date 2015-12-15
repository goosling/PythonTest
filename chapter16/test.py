__author__ = 'joe'
# !/usr/bin/env python
# -*-coding:utf-8-*-
from socket import *
import sys

website = sys.argv
port = 80
print website

print 'creating socket...'
s = socket(AF_INET, SOCK_STREAM)
print 'done...'

print 'connecting to..'
s.connect(website.port)

s.send("Get /index.html HTTP/1.0\r\n\r\n")
data = s.recv(4096)
print data