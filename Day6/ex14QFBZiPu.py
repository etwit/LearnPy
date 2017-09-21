#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月18日

@author: Ethan Wong
'''
#函数多线程
#生产者与消费之间 
#1.解耦问题，没生产完包子请等待5分钟 生产者和消费者只依赖缓冲区，而不互相依赖
#2.支持并发和异步
#3.支持忙闲不均

import random
import time
import Queue
import threading


def Proudcer(name,que):
    while True:
        if que.qsize()<3:
            que.put('baozi')
            print '%s:Made a baozi========='% name
        else:
            print '还有剩余包子++++++'
        time.sleep(random.randrange(3))

def Consumer(name,que):
    while True:
        try:
            que.get_nowait()
            print '%s:Got a baozi...' % name
        except Exception:
            print '没有包子了...'
        time.sleep(random.randrange(3))
q = Queue.Queue()
p1 = threading.Thread(target=Proudcer,args=['chef1',q])
p2 = threading.Thread(target=Proudcer,args=['chef2',q])
p1.start()
p2.start()
c1 = threading.Thread(target=Consumer,args=['chengchao',q])
c2 = threading.Thread(target=Consumer,args=['yangkan',q])
c1.start()
c2.start()
