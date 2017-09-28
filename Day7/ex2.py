#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月19日

@author: Ethan Wong
'''
#进程与线程区别：
#1进程可以调用多个cpu 试用于计算密集型
#2线程是根据cpu的时间片 来对I/O进行操作 充分调用磁盘的性能 I/O密集型

#生产者和消费者模型 最大的特点
#1解耦 通过缓冲区来解耦数据
#2支持并发
#3支持忙闲不均 通过缓冲区缓冲

#多进程 multiprocessing

#通过进程池的方式启动多个进程
from multiprocessing import Pool
import time
def f(x):
    #print x*x
    return x*x
    time.sleep(1)
    
if __name__=='__main__':
    p=Pool(9)
    n = [0,1,2,3,4,5,6,7,8,9]
    print(p.map(f,n))
    
#通过主进程和子进程的方式调用
#多进程的时候注意 内存
from multiprocessing import Process
import os

def info(title):
    print title
    print 'module name:',__name__
    if hasattr(os,'getppid'):
        print 'parent process:',os.getppid()
    time.sleep(1)
    #print 'proccess id:',os.getppid()

def f1(name):
    info('function f1')
    print 'hello',name
    
if __name__ =='__main__':
    info('main line')
    p = Process(target=f1,args=('bob',))
    p.start()
    p.join()