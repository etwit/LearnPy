#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月15日

@author: Ethan Wong
'''
#socket 服务端

import socket

sk = socket.socket()

ip_port = ('127.0.0.1',9999)

sk.bind(ip_port)
sk. listen(5)

while True:
    conn,address = sk.accept()
    conn.send('hello.')
    flag = True
    while flag:
        #recv(1024)是缓冲区中最多只能拿到1024字节
        data = conn.recv(1024)
        print data
        if data == 'exit':
            flag = False
        conn.send('sb')
    conn.close()


