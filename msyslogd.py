# -*- coding:utf-8 -*-
# Author:niannun
# E-mail:niannun@126.com
import sys
import argparse
import socket
import time


class msyslogd(object):
    BUFSIZE = 1024
    def __init__(self, log_file, ip="0.0.0.0", port=514, **kwargs):
        self.ip = ip
        self.port = port
        if log_file:
            self.lffd = open(log_file, "a+")
        self.kwargs = kwargs

    def _udp_server(self):
        ip_port = (self.ip, self.port)
        upd_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        upd_server.bind(ip_port)
        i = 0
        messages = []
        ts = int(time.time())
        while True:
            tn = 0
            data, client = upd_server.recvfrom(self.BUFSIZE)
            if self.kwargs['o']:
                print data
            #need statistics
            if self.kwargs['s'] or self.lffd:
                messages.append(data)
                tn = int(time.time())
                if (tn - ts) == 1:
                    if self.lffd:
                        self.lffd.write(messages)
                        messages = []
                    ts = tn
            i = i + 1
        upd_server.close()
        self.lffd.close()

    def _calc_statistic(self, msg_size, time_second):
        pass

    def run(self):
        pass



def main():
    parser = argparse.ArgumentParser(description="msyslogd")
    parser.add_argument("-s", action="store_true", default=False, help="Do statistics")
    parser.add_argument("-o", action="store_true", default=False, help="Output logs to screen")
    parser.add_argument("-f", "--log-file", dest="logfile", type=str, help="specify log file")
    parser.add_argument("-p", "--port", dest="port", type=int, default=514, help="specify the port to listen on")
    parser.add_argument("-a", "--ip-address", dest="IPaddress", type=str, default="0.0.0.0", help="specify the IP to listen on")
    args = parser.parse_args()
    print args    

if __name__ == "__main__":
    sys.exit(main())