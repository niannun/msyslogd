#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:niannun
# E-mail:niannun@126.com

import socket
import sys
import time

f = file("./messages",'r')
address = ('10.180.15.150', 514)

level = 2
facility = 2
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ts = int(time.time()) 
while True:
    line = f.readline().strip()
    if len(line) == 0:
        break
    msg = '<%d> %s' % (level+facility, line)
    s.sendto(msg, address)
    #time.sleep(0.0001)
te = int(time.time())
print "%d seconds" % ((te-ts),)
f.close()
s.close()