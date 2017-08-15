#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年8月15日

@author: Ethan Wong
'''
'''
ThreadingTCPServer 首先继承
BaseServer
--:__init__
self.server_address = ('127.0.0.1',9999)
self.RequestHandlerClass = MyServer

TCPServer    ThreadingMixIn
--:__init__
     BaseServer.__init__(self, server_address, RequestHandlerClass)

ThreadingTCPServer 首先继承

server = ThreadingTCPServer(('127.0.0.1',9999),MyServer)
server.serve_forever()

'''
import SocketServer
class  MyServer(SocketServer.BaseRequestHandler):
    
    def setup(self):
        pass

    def handle(self):
        print self.request,self.client_address,self.server
        #self.request = socket
        #

    def finish(self):
        pass
        
if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    server.serve_forever()