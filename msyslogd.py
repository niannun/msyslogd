# -*- coding:utf-8 -*-
# Author:niannun
# E-mail:niannun@126.com
import sys
import argparse


class msyslogd(object):
    pass


def main():
    parser = argparse.ArgumentParser(description="msyslogd")
    parser.add_argument("-s", action="store_true", default=False, help="Do statistics")
    parser.add_argument("-f", "--log-file", dest="logfile", type=str, help="specify log file")
    parser.add_argument("-o", action="store_true", default=False, help="Output logs to screen")
    args = parser.parse_args()
    print args    

if __name__ == "__main__":
    sys.exit(main())