#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:niannun
# E-mail:niannun@126.com

import syslog

syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_MAIL)
syslog.syslog('E-mail processing initiated...')