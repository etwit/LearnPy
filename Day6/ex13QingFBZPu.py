#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月15日

@author: Ethan Wong
'''
from threading import Thread
from Queue import Queue
import time


#创建一个队列 先进先出
#生产者与消费之间 
#1.解耦问题，没生产完包子请等待5分钟 生产者和消费者只依赖缓冲区，而不互相依赖
#2.支持并发和异步
#3.支持忙闲不均

class Procuder(Thread):
    
    #name 生产者的名子 queue 容器
    def __init__(self,name,queue):
        self.__Name = name
        self.__Queue = queue
        #执行父类的函数
        super(Procuder,self).__init__()
        
    def run(self):
        while True:
            if self.__Queue.full():
                time.sleep(2)
            else:
                self.__Queue.put('baozi')
                time.sleep(1)
                print'%s 生产了一个包子 '%(self.__Name,)
        #Thread.run(self)
    
class Consumer(Thread):
    
    #name 消费者的名子 queue 容器
    def __init__(self,name,queue):
        self.__Name = name
        self.__Queue = queue
        super(Consumer,self).__init__()
    
    def run(self):
        while True:
            if self.__Queue.empty():
                time.sleep(2)
            else:
                self.__Queue.get()
                time.sleep(1)
                print'%s 消费了一个包子 '%(self.__Name,)
        #self.__Queue.get()
        #Thread.run(self)

que = Queue(maxsize=100)

laogou1 = Procuder('老狗1',que)
laogou1.start()
laogou2 = Procuder('老狗2',que)
laogou2.start()
laogou3 = Procuder('老狗3',que)
laogou3.start()

for item in range(20):
    name = 'chengtao%d'%(item,)
    temp = Consumer(name,que)
    temp.start()

'''
print que.qsize()
que.put('1')
que.put('2')

print que.qsize()
print 'get:',que.get()
print 'get:',que.get()
print 'empty:',que.empty()
'''