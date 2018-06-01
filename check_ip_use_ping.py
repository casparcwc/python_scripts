#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:casparcc
'''
stdout: 100% packet loss ip
'''

import os, sys, re
import subprocess


def NetCheck(ip):
    try:
        #fhandle = open(r'dns_unknow_ip.txt','a')
        #p2 = subprocess.Popen(["ping -c 1 -w 1 " + ip], stdout=fhandle, shell=True)
        #fhandle.close()
        p = subprocess.Popen(["ping -c 1 -w 1 " + ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out = p.stdout.read()
        #err=p.stderr.read()
        regex = re.compile('100% packet loss')
        #print p.stdout.read()
        # print regex
        if len(regex.findall(out)) == 0:
            #print ip + ': host up'
            return 'up'
        else:
            #print ip + ': host down'
            return 0
    except Exception,e:
        print e
        return e

def check_ip(ip):
    try:
        p = os.popen("ping -c 1 -w 1 " + ip)
        out = p.read()
        regex = re.compile('100% packet loss')
        if len(regex.findall(out)) == 0:
            return 'up'
        else:
            return False
    except Exception,e:
        print e
        return e


if __name__ == '__main__':
    with open("dns_ip.txt") as ipfile:
        ip = ipfile.readline()
        unknow_ip_list=[]
        for i in ipfile.readlines():
            status = check_ip(i)
            if not status:
                unknow_ip_list.append(i)
        for j in unknow_ip_list:
            print j
