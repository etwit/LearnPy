#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月13日

@author: Ethan Wong
'''

#GIL 全局解释器锁
#应用程序编写
#多进程应用场景：计算密集型 进过cpu计算 用多进程
#多线程场景:I/O操作

from threading import Thread
import time

'''def Foo(arg,v):
    print arg

print 'before'

t1 = Thread(target=Foo,args=(1,11,))
t1.start()
print 'after'
'''



def Foo(arg,v):
    for item in range(5):
        print item
        time.sleep(1)
        

print 'before'

t1 = Thread(target=Foo,args=('dddd',11,))
#是否为守护进程
#t1.setDaemon(True)
t1.start()
#获取线程名
print t1.getName()
#子线程的执行时间 只等你三秒
t1.join(3)
print 'after'
print 'after end'





'''t2 = Thread(target=Foo,args=('dddd',11,))

t2.start()
print t2.getName()'''

