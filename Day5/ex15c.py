#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月15日

@author: Ethan Wong
'''
#socket 客户端

import socket

client = socket.socket()
ip_port =('127.0.0.1',9999)

client.connect(ip_port)


while True:
    data = client.recv(1024)
    print data 
    inp = raw_input('clent:')
    client.send(inp)
    if inp == 'exit':
        break