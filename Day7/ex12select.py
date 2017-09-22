#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月22日

@author: Ethan Wong
'''
#Select vs poll &epoll
#异步io模型
#最大端口数 65535
#ulimit -n 查看

#select，poll，epoll都是IO多路复用的机制。I/O多路复用就是通过一种机
#制使一个进程可以监视多个描述符，一旦某个描述符就绪（一般是读就绪或者写就绪），
#能够通知程序进行相应的读写操作。
#select，poll，epoll本质上都是同步I/O，因为他们都需要在读写事件就绪
#后自己负责进行读写，也就是说这个读写过程是阻塞的
#异步I/O则无需自己负责进行读写，异步I/O的实现会负责把数据从内核拷贝到用户空间。
