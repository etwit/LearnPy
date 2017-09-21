#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月15日

@author: Ethan Wong
'''
#自定义线程类
from threading import Thread
import time

class MyThread(Thread):
    
    def run(self):
        # Bar()
        time.sleep(3)
        print '我实习线程'
        #调用父类run方法
        Thread.run(self)
        

def Bar():
    print 'bar'
    
t1 = MyThread(target=Bar)
t1.start()
print 'over\n'












'''def func1():
    print 'func1'
    func2()
    
def func2():
    print 'func2'

func1()'''


